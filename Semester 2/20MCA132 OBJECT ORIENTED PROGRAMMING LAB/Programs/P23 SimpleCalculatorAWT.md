# Program 23 - Simple Calculator using AWT

## Question

Implement a simple calculator using AWT components.

---

# Filename

```text
P23_SimpleCalculatorAWT.java
```

---

# Source Code

```java
import java.awt.*;
import java.awt.event.*;

public class P23_SimpleCalculatorAWT extends Frame implements ActionListener
{
    private TextField textField;
    private Button[] numberButtons;
    private Button[] operationButtons;
    private Button equalsButton;
    private Button clearButton;
    private double num1,num2,result;
    private char operation;

    public P23_SimpleCalculatorAWT()
    {
        setTitle("Simple Calculator");
        setSize(300,400);
        setLayout(new BorderLayout());

        textField=new TextField();
        textField.setEditable(false);
        add(textField,BorderLayout.NORTH);

        Panel buttonPanel=new Panel();
        buttonPanel.setLayout(new GridLayout(4,4));

        numberButtons=new Button[10];

        for(int i=0;i<10;i++)
        {
            numberButtons[i]=new Button(String.valueOf(i));
            numberButtons[i].addActionListener(this);
            buttonPanel.add(numberButtons[i]);
        }

        operationButtons=new Button[4];

        operationButtons[0]=new Button("+");
        operationButtons[1]=new Button("-");
        operationButtons[2]=new Button("*");
        operationButtons[3]=new Button("/");

        for(int i=0;i<4;i++)
        {
            operationButtons[i].addActionListener(this);
            buttonPanel.add(operationButtons[i]);
        }

        equalsButton=new Button("=");
        equalsButton.addActionListener(this);
        buttonPanel.add(equalsButton);

        clearButton=new Button("C");
        clearButton.addActionListener(this);
        buttonPanel.add(clearButton);

        add(buttonPanel,BorderLayout.CENTER);

        addWindowListener(new WindowAdapter()
        {
            public void windowClosing(WindowEvent windowEvent)
            {
                System.exit(0);
            }
        });
    }

    public void actionPerformed(ActionEvent ae)
    {
        String command=ae.getActionCommand();

        if(command.charAt(0)>='0' && command.charAt(0)<='9')
        {
            textField.setText(textField.getText()+command);
        }

        else if(command.charAt(0)=='C')
        {
            textField.setText("");
        }

        else if(command.charAt(0)=='=')
        {
            num2=Double.parseDouble(textField.getText());

            switch(operation)
            {
                case '+':
                    result=num1+num2;
                    break;

                case '-':
                    result=num1-num2;
                    break;

                case '*':
                    result=num1*num2;
                    break;

                case '/':
                    if(num2!=0)
                    {
                        result=num1/num2;
                    }

                    else
                    {
                        textField.setText("Cannot divide by zero");
                    }

                    break;
            }

            textField.setText(String.valueOf(result));
        }

        else
        {
            num1=Double.parseDouble(textField.getText());
            operation=command.charAt(0);
            textField.setText("");
        }
    }

    public static void main(String[] args)
    {
        P23_SimpleCalculatorAWT calculator=new P23_SimpleCalculatorAWT();

        calculator.setVisible(true);
    }
}
```

---

# Concepts Used

- AWT Components
- Event Handling
- GUI Programming
- Frame
- Button
- TextField
- Layout Managers
- ActionListener
- WindowAdapter

---

# Theory

AWT stands for:
```text
Abstract Window Toolkit
```

It is Java’s:
```text
GUI library
```

used for:
- windows
- buttons
- text fields
- user interfaces

---

# GUI Programming

GUI means:
```text
Graphical User Interface
```

Users interact using:
- buttons
- windows
- mouse
- keyboard

---

# Frame

```java
Frame
```

is:
```text
top-level window
```

used for creating GUI applications.

---

# ActionListener

```java
ActionListener
```

handles:
```text
button click events
```

---

# actionPerformed()

```java
public void actionPerformed(ActionEvent ae)
```

is automatically called:
```text
when button clicked
```

---

# TextField

```java
TextField
```

used for:
```text
displaying input and result
```

---

# Buttons Used

| Button | Purpose |
|---|---|
| 0-9 | Number input |
| + | Addition |
| - | Subtraction |
| * | Multiplication |
| / | Division |
| = | Calculate result |
| C | Clear display |

---

# Layout Managers

## BorderLayout

Used for:
```text
arranging components in regions
```

---

## GridLayout

Used for:
```text
button grid arrangement
```

---

# Event Handling

When user clicks button:
1. Event generated
2. actionPerformed() called
3. Corresponding operation executed

---

# WindowAdapter

Used for:
```text
handling window closing event
```

---

# Division by Zero

Handled using:
```java
if(num2!=0)
```

Otherwise:
```text
Cannot divide by zero
```

displayed.

---

# Detailed Algorithm

1. Import AWT packages.

2. Create class extending:
```java
Frame
```

3. Implement:
```java
ActionListener
```

4. Declare:
- TextField
- Buttons
- Variables

5. Set:
- title
- size
- layout

6. Create text field.

7. Create button panel.

8. Create number buttons.

9. Create operation buttons.

10. Add listeners.

11. Add buttons into panel.

12. Add panel into frame.

13. Add window listener.

14. Implement:
```java
actionPerformed()
```

15. Handle:
- numbers
- operations
- equals
- clear

16. Perform calculations.

17. Display result.

18. Create calculator object.

19. Make frame visible.

20. Stop program.

---

# Flow of Execution

```text
Start
   ↓
Create Frame
   ↓
Add TextField
   ↓
Create Buttons
   ↓
Add ActionListeners
   ↓
Display GUI
   ↓
User Clicks Button
   ↓
actionPerformed()
   ↓
Perform Operation
   ↓
Display Result
   ↓
Stop
```

---

# Sample Operations

## Addition

Input:
```text
5 + 3
```

Output:

:contentReference[oaicite:0]{index=0}

---

## Subtraction

:contentReference[oaicite:1]{index=1}

---

## Multiplication

:contentReference[oaicite:2]{index=2}

---

## Division

:contentReference[oaicite:3]{index=3}

---

# Internal Working

Calculator stores:
```text
first number
```

when operation selected.

Second number stored:
```text
after pressing =
```

Operation executed using:
```java
switch
```

statement.

---

# Time Complexity

Button operation:

:contentReference[oaicite:4]{index=4}

---

# Space Complexity

:contentReference[oaicite:5]{index=5}

---

# Advantages

- Interactive GUI
- Event driven programming
- Easy calculations
- User friendly interface

---

# Limitations

- Handles only basic operations
- No decimal button
- No scientific calculations

---

# Edge Cases

## Case 1: Division by Zero

Displays:
```text
Cannot divide by zero
```

---

## Case 2: Empty Input

May cause:
```text
NumberFormatException
```

---

## Case 3: Multiple Operations

Only one operation handled at a time.

---

# Possible Improvements

- Add decimal point
- Add scientific functions
- Add keyboard support
- Improve GUI design

---

# Possible Errors

## 1. NumberFormatException

Occurs for invalid input.

---

## 2. Arithmetic Error

Division by zero.

---

# Viva Questions

## Q1. What is AWT?
Java GUI toolkit.

---

## Q2. What does AWT stand for?
Abstract Window Toolkit.

---

## Q3. Which class creates window?

```java
Frame
```

---

## Q4. Which interface handles button events?

```java
ActionListener
```

---

## Q5. Which method handles events?

```java
actionPerformed()
```

---

## Q6. Which layout used for buttons?

```java
GridLayout
```

---

## Q7. Which layout used for frame?

```java
BorderLayout
```

---

## Q8. Which component displays text?

```java
TextField
```

---

## Q9. Time complexity of operations?

:contentReference[oaicite:6]{index=6}

---

## Q10. What is event handling?
Responding to user actions like button clicks.