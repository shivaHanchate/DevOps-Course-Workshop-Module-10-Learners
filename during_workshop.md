# Module 10 Workshop

## Pre-requisites

You need to have an azure account. You can create a free acount [here](https://azure.microsoft.com/en-us/free/?WT.mc_id=A261C142F).

Also make sure you have installed the following:
- [Visual Studio Code](https://code.visualstudio.com/download)
    - Make sure you have the [C# extension](https://marketplace.visualstudio.com/items?itemName=ms-dotnettools.csharp)
- [Git](https://git-scm.com/)
- [.NET Core 3.1](https://dotnet.microsoft.com/download)

## Part 1 - Protected web api

We want to create a web api which is protected by [Azure Active Directory authentication](https://docs.microsoft.com/en-us/azure/active-directory/authentication/overview-authentication#:~:text=One%20of%20the%20main%20features,of%20a%20username%20and%20password.). 
That means it shouldn't be possible to access the api without a valid authentication token. We'll use Azure services to generate and verify the token.

### 1.1: Setup the web API
This repository contains code for a simple .NET Core web API. 
It exposes one GET endpoint, WeatherForecast, which will return a randomly generated weather forecast for the next five days.
As you'll be building on this code, it's recommended that you [fork](https://docs.github.com/en/github/getting-started-with-github/fork-a-repo) the repository like you did for workshop 7 and 8.

You don't need to worry too much about what the code is doing for now, however you should be able to build and run the app.

1. Run `dotnet build` from the terminal in the project folder.
2. Run `dotnet run` from the terminal in the project folder.
3. Go to https://localhost:5001/swagger/index.html in the browser. This loads a [Swagger UI](https://swagger.io/tools/swagger-ui/) page.  Swagger UI is a useful tool to test API endpoints. To test this API click the "/WeatherForecast" row then "Try it out" then "Execute". You should then be able to see the response from the endpoint.

![Swagger UI](img/SwaggerUI.png)

### 1.2: Create Azure AD Tenant
The first step is to create an Azure AD Tenant. A tenant in this case is an instance of Azure Active Directory.

Follow [these instructions](https://docs.microsoft.com/en-us/azure/active-directory/develop/quickstart-create-new-tenant#create-a-new-azure-ad-tenant) to create a tenant to use. In particular you want to create a new Azure AD Tenant, you don't want to use an existing one.

### 1.3: Create an app registration for a protected web API
The next step is to create an app registration for the web API we're going to use.  We need to do this so that we can verify the authentication token sent to our API is valid.  To do this we register our application with our tenant as a protected web api. 

In particular we want to configure it so that it can be called by a daemon app. That means an application can request a token to access it, instead of needing a user to log in first.

There's an [official microsoft guide](https://docs.microsoft.com/en-us/azure/active-directory/develop/quickstart-register-app) for how to create an app registration in general and [this guide](https://docs.microsoft.com/en-us/azure/active-directory/develop/scenario-protected-web-api-app-registration) explains what in particular you need to do for a protected web api.

However those guides can be a bit confusing, as you only need to follow some of the steps. So I'd recommend following "Register the service app" section of [this guide](https://github.com/Azure-Samples/active-directory-dotnetcore-daemon-v2/tree/master/2-Call-OwnApi#register-the-service-app-todolist-webapi-daemon-v2). That guide is specifically for the scenario we're interested in so should be easier to follow. In particular the steps you need to do are:
1. Create a new app registration.
2. Expose an api on your app registration.
3. Expose application permissions. This is necessary so that the API can be accessed by a daemon app instead of a signed in user.

### 1.4: Add authentication to a web API
Now we need to add some code to our API so that it will only allow requests with the correct authentication.

There are a few changes we need to make:
1. Add the Azure AD config from the app registration to the app. See [this guide](https://docs.microsoft.com/en-us/azure/active-directory/develop/scenario-protected-web-api-app-configuration#config-file) for what the format of the config should be. In particular you need the Directory (tenant) ID and the Application (client) ID for your app registration. You can find that on the overview page for your app registration in the Azure portal. This should be added to the `appsettings.json` file.

2. Configure the app to use authentication. These changes need to be made in `Startup.cs`. You need to update the `ConfigureService` method so that it sets up the authentication using the config values from appsettings.json (passed in through the IConfiguration object). You also need to update the `Configure` method so that it adds authentication and authorization to the app. See [this guide](https://docs.microsoft.com/en-us/azure/active-directory/develop/scenario-protected-web-api-app-configuration#starting-from-an-existing-aspnet-core-31-application) for details.

3. Add authentication to the `WeatherForecast` endpoint. See [this guide](https://docs.microsoft.com/en-us/azure/active-directory/develop/scenario-protected-web-api-verification-scope-app-roles#verify-app-roles-in-apis-called-by-daemon-apps) for details. We want to make sure our controller is protected with the `Authorize` attribute, this will ensure it's not possible to hit the endpoint without a valid token. And we want to verify that the token is for `access_as_application`, meaning that access has been granted to an application rather than a signed in user.

The API should now be protected. If you try to hit the endpoint again through Swagger UI, you should get a 401 error response. This means that the request has been rejected because you didn't provide the correct authentication.

You'll see in the next part how we can add a valid authentication token to the request.

## Part 2 - Access a protected web API

### 2.1: Create an app registration for a client accessing the web API

To generate a valid token we first need to create a second app registration in the Azure portal. This is to register the application which will be requesting access to the API. To do this follow the ["Register the client app" section](https://github.com/Azure-Samples/active-directory-dotnetcore-daemon-v2/tree/master/2-Call-OwnApi#register-the-client-app-daemon-console) of the same guide you used to create the first app registration. In particular make sure you grant API permission for the new application to access the first app registration you created, as per step 5 in the guide. And make sure you grant admin constent for the tenant on the API permissions page. As you created the tenant you should have admin permissions to do so.

### 2.2: Get a token to access the web API

You should now be able to request a token to access the API. You can do this by just using `curl` in the terminal. See [here](https://docs.microsoft.com/en-us/azure/active-directory/develop/v2-oauth2-client-creds-grant-flow#first-case-access-token-request-with-a-shared-secret) for what the request should look like. In particular:
* The tenant id should be from the tenant you created in part 1. You can find this on the overview page for either of the app registrations you've created.
* The client id should be the client id for the app registration you created in step 2.1.
* The scope should be the application ID URI from the first app registration you created in step 1.3 followed by ".default" and it needs to be URI encoded. For example `api%3A%2F%2F40ae91b7-0c83-4b5c-90f3-40187e8f2cb6%2F.default` would be the correct scope for application ID URI api://40ae91b7-0c83-4b5c-90f3-40187e8f2cb6. You can find the application ID URI by going to the "Expose an API" section for your first app registration in the Azure portal.
* The client secret should be the one you created in step 2.1.

Once you get a successful response copy the access token from it. You're going to use this in the request to your web API.

### 2.3: Send a request to the web API

Now you just need to add the token from the previous step to your request to the API. Luckily we can do this through swagger UI.

With the web API running and the Swagger UI page open you should see an "Authorize" button. The button should currently have an unlocked padlock icon on it, which means that no authorization token has been added. Once you click the button a popup should appear where you can enter the token. Make sure to include "Bearer" but don't include quotes. So for example:
```
Bearer eyJ0eXAiOiJKV1QiLCJ...
```

After you've entered the token click "Authorize".  This should close the popup and the "Authorize" button should now have a closed padlock icon on it. When you now send a request through Swagger it should include the token and the request should be accepted.
