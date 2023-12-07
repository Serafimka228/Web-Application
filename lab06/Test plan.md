# Test Plan

---

## Contents

1 [Introduction](#introduction)  
2 [Test items](#test-items)  
3 [Quality attributes](#quality-attributes)  
4 [Risks](#risks)  
5 [Aspects to be tested](#aspects-to-be-tested)  
6 [Testing approaches](#testing-approaches)  
7 [Test results](#test-results)  
8 [Conclusion](#conclusion)

## Introduction

This document describes the testing plan of the WEB-application ["Music rating application"](https://github.com/Serafimka228/Web-Application/tree/main/lab05/web%20application).  
The document is intended for QA.  
The purpose of testing is to check if the real behavior of the project program corresponds to its expected behavior. The expected results are formed on the basis of [requirements](https://github.com/savkunok/RateYourMusic/blob/main/Requirements.md).

## Test items

As test objects we can single out program modules responsible for the fulfillment of [functional requirements](https://github.com/savkunok/RateYourMusic/blob/main/Requirements.md), as well as displays of the main parts of the user interface:

- User registration
- User login
- User logout
- Search albums
- Rate albums

## Quality attributes

1. Functionality:
   - Functional completeness: the application must perform all stated [functions](https://github.com/savkunok/RateYourMusic/blob/main/Requirements.md);
   - functional correctness: the application must perform all declared functions correctly;
   - functional appropriateness: there are no functions not declared that would prevent the application from fulfilling its original purpose.
2. Usability:
   - User interface aesthetics: use of successful design solutions, clear and modern interface;
   - Relevance: updating data, e.g. information on product availability;

## Risks

In this case, the risks may include:

- API change;
- Absence of Internet connection when working with the application;
- Changes in the current standards of html-documents displaying in different browsers;
- Internet connection interruption when running a test in which it is provided;

## Aspects to be tested

During testing it is planned to check the implementation of the main functions of the application. Aspects to be tested:

1 [Running the WEB-application](#running-the-web-application);  
2 [Navigate between application pages](#navigate-between-application-pages);  
3 [Search album interaction](#task-list-interaction);  
4 [User authentication](#user-authentication).

Note: An Internet connection is assumed when testing all aspects.

### Running the WEB-application

This use case should be tested on:

- Running the application without an internet connection;
- Running an application with an internet connection.

### Navigate between application pages

This use case should be tested on:

- Go to the home page;
- Go to the album page;
- Go to the sign in/sign up page.

### Search album interaction

This use case should be tested on:

- Search album;

### User authentication

This use case should be tested on:

- Correct login;
- Correct sign-up.

## Non-functional requirements:

The WEB application must also comply with the previously the previously defined ["non-functional requirements"](https://github.com/savkunok/RateYourMusic/blob/main/Requirements.md).

## Testing approaches

A manual approach will be used for testing.

## Test results

The results are presented in the document ["Test results"]([https://github.com/Serafimka228/Web-Application/tree/main/lab05/web%20application/Test%20results.md](https://github.com/Serafimka228/Web-Application/blob/main/lab06/Test%20results.md)).

## Conclusion

This test plan allows you to test the basic functionality of the application. Successful passing of all tests does not guarantee full functionality on all versions of web browsers, but it allows you to assume that the software works correctly. At the moment of the application development completion, the testing has been successfully passed. In the future, when expanding the functionality of the WEB-application, it will be necessary to create new tests to verify the compliance of the product with the previously specified requirements.
