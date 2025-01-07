## Testing

### 1\. **Testing Methodology**

#### **Unit Testing**

-   Core game functions were tested in isolation to ensure they work as intended.
-   Focus areas:
    -   Board initialization.
    -   Ship placement validation.
    -   Attack logic (hit, miss, repeat).
    -   Game-ending conditions.

#### **Integration Testing**

-   Verified that all components work seamlessly together in a complete game session.

#### **Manual Testing**

-   Simulated multiple game sessions to test user interactions and edge cases.

#### **Static Code Analysis**

-   Used linting tools to identify and fix formatting issues and coding standard violations.

* * * * *

### 2\. **Tools Used**

-   **Linting**: `flake8` and `black` for PEP 8 compliance and formatting.
-   **Manual Testing**: Command-line execution.

* * * * *

### 3\. **Test Cases**

#### **Unit Tests**

| Feature | Test Case Description | Result |
| --- | --- | --- |
| Board Initialization | Verify the board initializes with correct dimensions and empty cells. | ✅ Passed |
| Ship Placement | Ensure valid placement of ships and rejection of overlaps or out-of-bounds positions. | ✅ Passed |
| Attack Logic | Validate outcomes for hits, misses, and repeated coordinates. | ✅ Passed |
| Game End Condition | Confirm the game ends correctly when all ships are sunk. | ✅ Passed |

#### **Edge Cases**

| Scenario | Test Case Description | Result |
| --- | --- | --- |
| Invalid Input Handling | Reject non-numeric or improperly formatted inputs gracefully. | ✅ Passed |
| Boundary Conditions | Prevent out-of-bound attacks or placements. | ✅ Passed |

* * * * *

### 4\. **Static Code Analysis**

-   **Flake8 Results**:
    -   **Warnings**: Addressed all `E501: line too long` warnings.
    -   **Other Issues**: No other significant violations found.

* * * * *

### 5\. **Testing Results**

| Type of Test | Status |
| --- | --- |
| Unit Testing | ✅ Completed |
| Integration Testing | ✅ Completed |
| Manual Testing | ✅ Completed |
| Static Code Analysis | ✅ Completed |

* * * * *
