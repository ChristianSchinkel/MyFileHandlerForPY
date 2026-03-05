"""
basic_py_package: A basic Python package template.

This package provides a simple example of a Python package structure
that can be installed via pip install.
"""

__version__ = "0.1.0"
__author__ = "Christian Schinkel"
__all__ = ["greet", "add", "multiply"]


def greet(name: str = "World") -> str:
    """
    Return a greeting message.
    
    Args:
        name: The name to greet (default: "World")
        
    Returns:
        A greeting string
        
    Example:
        >>> greet("Alice")
        'Hello, Alice!'
    """
    return f"Hello, {name}!"


def add(a: float, b: float) -> float:
    """
    Add two numbers together.
    
    Args:
        a: First number
        b: Second number
        
    Returns:
        Sum of a and b
        
    Example:
        >>> add(2, 3)
        5
    """
    return a + b


def multiply(a: float, b: float) -> float:
    """
    Multiply two numbers together.
    
    Args:
        a: First number
        b: Second number
        
    Returns:
        Product of a and b
        
    Example:
        >>> multiply(2, 3)
        6
    """
    return a * b
