"""Operating System check utils."""
import platform


class OpereatingSystem:
    """Operating System check utils."""

    @staticmethod
    def is_windows() -> bool:
        """Check if the operating system is Windows."""
        return platform.system() == "Windows"

    @staticmethod
    def is_linux() -> bool:
        """Check if the operating system is Linux."""
        return platform.system() == "Linux"

    @staticmethod
    def is_mac() -> bool:
        """Check if the operating system is macOS."""
        return platform.system() == "Darwin"


def main():
    """Main function to demonstrate the operating system check."""
    os_checker = OpereatingSystem()
    if os_checker.is_windows():
        print("You are using Windows.")
    elif os_checker.is_linux():
        print("You are using Linux.")
    elif os_checker.is_mac():
        print("You are using macOS.")
    else:
        print("Unknown operating system.")


if __name__ == "__main__":
    main()
