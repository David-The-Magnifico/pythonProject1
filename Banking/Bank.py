case 1:
    System.out.print("Enter name: ");
    String name = scanner.next();
    System.out.print("Enter PIN: ");
    String pin = scanner.nextLine();
    bank.registerCustomer(name, pin);
    System.out.println("Account registered successfully.");
    break;
