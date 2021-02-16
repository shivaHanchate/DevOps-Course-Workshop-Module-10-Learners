# During the Workshop

Before starting make sure you have addressed the prerequisites in the <README.md>.

## Part 1 Threat Modelling

In the first part of today's workshop you will be conducting a security review of an organisation's IT systems. You will be provided with a description of the system and potentially some diagrams. Threat modelling can be an open ended process, so your trainers will probably time box each section of the exercise.

### Identify Threats

The first thing we need to do is to try to identify the possible threats the system could face. This is not an easy task: there are lots of possible attack vectors and many different sorts of threats.

Use the **STRIDE** topics as guidance and work your way through the systems methodically, perhaps system by system. At the end of this process you should have a list of potential threats grouped by topic and system. (You will probably find it helpful to record these in a spreadsheet.)

#### STRIDE

A reminder from the reading material.

- **Spoofing** - impersonating another user or application
- **Tampering** - modifying input to execute an attack (e.g. the injection attacks from previous chapters)
- **Repudiation** - performing an action that cannot definitively be traced to the attacker
- **Information disclosure** - leak of sensitive data, a data breach
- **Denial of service** - rendering the application unavailable
- **Elevation of privilege** - gaining access to resources that would otherwise be protected

### Assessing Likelihood and Severity

Once you have assembled your list of potential threats it is time to assess how risky they are. For each threat you should estimate its **likelihood**, the chance of it happening; and its **severity**, how bad it would be. There are many ways to do this, perhaps the simplest is to assign one of three categories for each axis, e.g. low, medium, or high. Once done you will be able to combine likelihood and severity to determine which threats you should prioritise.

Suggested prioritisation matrix:

|                   | Low Impact | Medium Impact | High Impact |
| ----------------- | ---------- | ------------- | ----------- |
| Low Likelihood    | LOW        | LOW           | MEDIUM      |
| Medium Likelihood | LOW        | MEDIUM        | HIGH        |
| High Likelihood   | MEDIUM     | HIGH          | HIGH        |

### Mitigating Risks

Finally, work through the prioritised list of threats and suggest ways to mitigate those risks. These don't have to be technical solutions; it can be cheaper **and** more effective to put a non-technical control in place instead.

## Part 2 Auth

This part of the workshop is in covered in [Part 2](./part_2.md).

## Part 3 XSS Training (Optional)

XSS bugs are extremely common. Google have developed a game that helps demonstrate how some of these work.

You can find the game [here](https://xss-game.appspot.com/) and work through it.

## Part 4 Vulnerable Docker Box (Optional)

A more varied option is the Damn Vulnerable Web Application. It is a deliberately vulnerable web application to let you safely and _legally_ explore breaking into a system. To make it easy to run locally there is a docker container provided - quick start instructions below. It is largely self-explanatory but for more detailed instructions go to [README.md](https://github.com/opsxcq/docker-vulnerable-dvwa/blob/master/README.md).

### Quick Start Instructions

Run the following docker command

```bash
    docker run --rm -it -p 80:80 vulnerables/web-dvwa
```

Visit `localhost` on your machine and authenticate with `Username: admin` and `Password: password`.
