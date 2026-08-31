# Core Feature Testing

## Student Performance Detection System

### Week 3: Testing of Core Features

This document records the testing of the core features of the initial prototype.

## Test Results

| Test ID | Feature | Test Input/Action | Expected Result | Actual Result | Status |
|---|---|---|---|---|---|
| TC01 | Valid Student ID Search | 28400 | Student record and details are displayed | Student record displayed successfully | PASS |
| TC02 | Another Valid Student ID Search | 65002 | Correct student record and details are displayed | Student record displayed successfully | PASS |
| TC03 | Invalid Student ID | 99999999 | Student ID not found message is displayed | Student ID not found in dataset message displayed | PASS |
| TC04 | Non-Numeric Input Validation | abc | Error message requesting a valid numeric Student ID | Please enter a valid numeric ID message displayed | PASS |
| TC05 | Empty Input Handling | Empty input | Application remains stable and performs no search | No action occurred and application remained stable | PASS |
| TC06 | Application and Dataset Loading | Refresh application | Application loads without errors | Application loaded normally with no errors | PASS |

## Summary

A total of six core test cases were conducted on the initial prototype. All six test cases passed successfully.

The tested features include valid and invalid Student ID searches, input validation, empty input handling, and application and dataset loading.

The results confirm that the current core features of the prototype are functioning as expected.