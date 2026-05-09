# Program 24 - Mouse Events and Window Events

## Question

Develop a program to handle all mouse events and window events.

---

# Filename

```text
P24_MouseEvents.java
```

---

# Source Code

```java
import javax.swing.*;
import java.awt.event.*;

public class P24_MouseEvents extends JFrame
{
    public P24_MouseEvents()
    {
        setTitle("Mouse Events Demo");

        setSize(400,300);

        setDefaultCloseOperation(JFrame.EXIT_ON_CLOSE);

        addMouseListener(new MouseAdapter()
        {
            public void mouseClicked(MouseEvent e)
            {
                System.out.println("Mouse clicked at ("+e.getX()+", "+e.getY()+")");
            }

            public void mousePressed(MouseEvent e)
            {
                System.out.println("Mouse pressed at ("+e.getX()+", "+e.getY()+")");
            }

            public void mouseReleased(MouseEvent e)
            {
                System.out.println("Mouse released at ("+e.getX()+", "+e.getY()+")");
            }

            public void mouseEntered(MouseEvent e)
            {
                System.out.println("Mouse entered at ("+e.getX()+", "+e.getY()+")");
            }

            public void mouseExited(MouseEvent e)
            {
                System.out.println("Mouse exited at ("+e.getX()+", "+e.getY()+")");
            }
        });

        addMouseMotionListener(new MouseMotionAdapter()
        {
            public void mouseDragged(MouseEvent e)
            {
                System.out.println("Mouse dragged to ("+e.getX()+", "+e.getY()+")");
            }

            public void mouseMoved(MouseEvent e)
            {
                System.out.println("Mouse moved to ("+e.getX()+", "+e.getY()+")");
            }
        });

        addWindowListener(new WindowAdapter()
        {
            public void windowClosing(WindowEvent e)
            {
                System.out.println("Window closed");
            }
        });
    }

    public static void main(String[] args)
    {
        SwingUtilities.invokeLater(() ->
        {
            P24_MouseEvents demo=new P24_MouseEvents();

            demo.setVisible(true);
        });
    }
}
```

---

# Concepts Used

- Swing
- JFrame
- Mouse Events
- Window Events
- Event Handling
- MouseListener
- MouseMotionListener
- WindowListener
- Adapter Classes
- GUI Programming

---

# Theory

Swing is:
```text
Java GUI framework
```

used for creating:
- windows
- buttons
- graphical applications

---

# JFrame

```java
JFrame
```

is:
```text
top-level Swing window
```

used for GUI applications.

---

# Event Handling

An event is:
```text
user interaction with GUI
```

Examples:
- mouse click
- mouse movement
- window close

---

# Mouse Events

Mouse events occur when user:
- clicks mouse
- drags mouse
- moves mouse
- enters window
- exits window

---

# MouseListener

```java
MouseListener
```

handles:
- mouseClicked()
- mousePressed()
- mouseReleased()
- mouseEntered()
- mouseExited()

---

# MouseMotionListener

```java
MouseMotionListener
```

handles:
- mouseDragged()
- mouseMoved()

---

# WindowListener

```java
WindowListener
```

handles:
```text
window related events
```

---

# Adapter Classes

Adapter classes provide:
```text
empty implementation of listener methods
```

Examples:
- MouseAdapter
- MouseMotionAdapter
- WindowAdapter

This avoids implementing:
```text
all methods manually
```

---

# Mouse Coordinates

```java
e.getX()
e.getY()
```

return:
```text
mouse cursor position
```

---

# invokeLater()

```java
SwingUtilities.invokeLater()
```

ensures:
```text
GUI created safely in Event Dispatch Thread
```

---

# Event Dispatch Thread

EDT is:
```text
special thread for Swing components
```

Used for:
- GUI updates
- event handling

---

# Detailed Algorithm

1. Import Swing and event packages.

2. Create class extending:
```java
JFrame
```

3. Set:
- title
- size
- close operation

4. Add:
```java
MouseListener
```

5. Override:
- mouseClicked()
- mousePressed()
- mouseReleased()
- mouseEntered()
- mouseExited()

6. Add:
```java
MouseMotionListener
```

7. Override:
- mouseDragged()
- mouseMoved()

8. Add:
```java
WindowListener
```

9. Override:
```java
windowClosing()
```

10. Print event messages.

11. Use:
```java
invokeLater()
```

12. Create frame object.

13. Make frame visible.

14. Stop program.

---

# Flow of Execution

```text
Start
   ↓
Create JFrame
   ↓
Add Mouse Listener
   ↓
Add Mouse Motion Listener
   ↓
Add Window Listener
   ↓
Display Window
   ↓
User Performs Action
   ↓
Event Generated
   ↓
Corresponding Method Executes
   ↓
Display Coordinates
   ↓
Stop
```

---

# Mouse Events Demonstrated

| Event | Method |
|---|---|
| Mouse Click | mouseClicked() |
| Mouse Press | mousePressed() |
| Mouse Release | mouseReleased() |
| Mouse Enter | mouseEntered() |
| Mouse Exit | mouseExited() |
| Mouse Drag | mouseDragged() |
| Mouse Move | mouseMoved() |

---

# Window Event Demonstrated

| Event | Method |
|---|---|
| Window Close | windowClosing() |

---

# Sample Output

```text
Mouse clicked at (120, 140)

Mouse moved to (200, 150)

Mouse dragged to (250, 180)

Window closed
```

---

# Dry Run

User:
```text
moves mouse
```

Method called:
```java
mouseMoved()
```

Coordinates displayed.

---

User:
```text
clicks mouse
```

Method called:
```java
mouseClicked()
```

Coordinates printed.

---

# Internal Working

When mouse action occurs:
1. Event object created
2. Listener detects event
3. Corresponding method executes

---

# Event Object

```java
MouseEvent e
```

contains:
- mouse coordinates
- event type
- source component

---

# Time Complexity

Event handling:

:contentReference[oaicite:0]{index=0}

---

# Space Complexity

:contentReference[oaicite:1]{index=1}

---

# Advantages

- Interactive GUI
- Event driven programming
- Real-time mouse tracking
- Easy event handling using adapters

---

# Limitations

- Console based output
- No graphical drawing
- Continuous movement prints many lines

---

# Edge Cases

## Case 1: Fast Mouse Movement

Generates many events quickly.

---

## Case 2: Closing Window

Triggers:
```java
windowClosing()
```

---

## Case 3: Dragging Outside Window

Coordinates may stop updating.

---

# Possible Improvements

- Display coordinates inside window
- Add keyboard events
- Add drawing functionality
- Use custom graphics

---

# Possible Errors

## 1. GUI Not Visible

If:
```java
setVisible(true)
```

missing.

---

## 2. Event Not Triggered

If listener not added properly.

---

# Viva Questions

## Q1. What is Swing?
Java GUI framework.

---

## Q2. Which class creates Swing window?

```java
JFrame
```

---

## Q3. What is event handling?
Handling user interactions in GUI.

---

## Q4. Which listener handles mouse click?

```java
MouseListener
```

---

## Q5. Which method handles mouse movement?

```java
mouseMoved()
```

---

## Q6. What are adapter classes?
Classes with empty listener methods.

---

## Q7. Why use MouseAdapter?
Avoid implementing all listener methods.

---

## Q8. What does getX() return?
Mouse X coordinate.

---

## Q9. What is Event Dispatch Thread?
Special thread for Swing GUI updates.

---

## Q10. Time complexity of event handling?

:contentReference[oaicite:2]{index=2}