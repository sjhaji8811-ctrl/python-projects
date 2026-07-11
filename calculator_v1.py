 def add(a, b): return a + b
def subtract(a, b): return a - b
def multiply(a, b): return a * b
def divide(a, b):
  if b == 0: return "Error (Div by Zero)"
  return a / b
def calculate_power(base, exponent): return base ** exponent
def calculate_percentage(total, percent): return (total * percent) / 100
def calculate_triangle_area(base, height): return 0.5 * (base * height)
master_session_logs = []
print(" INITIALIZING COMPLETE CAPSTONE MULTI-ENGINE BLUEPRINT ")
while True:
  print("\n ====================================================================")
  print("     MASTER CONSOLE SYSTEM INTERFACE     ")
  print("=======================================================================")
  print("1. standard core Math (add/Sub/Mult//Div)")
  print("2. Advanced Operation (Power/Percents)")
  print("3. Geometric Calculation (triangle Area)")
  print("4. View Full Session Transaction Logs")
  print("5. Global System Shutdown Sequence")
  print("=======================================================================")
  choice = input("Select Operation domain (1-5): ").strip()
  if choice == "5":
    print(" Secure power down initialized. session records cleared from active RAM. Bye! ")
    break
  elif choice == "4":
    print("\n FORWARDING COMPLETE TRANSACTION REGISTRY...")
    print("-" * 65)
    if len(master_session_logs) == 0:
      print(" System Warning: Data storage banks are empty. ")
    else:
      for row in master_session_logs:
        print(f" Process: {row[0]:<15} | Equation: {row[1]:<20} | Yield: {row[2]}")
        print("-" * 65)
      print(f"Total compiled transaction indexed: {len(master_session_logs)}")
  elif choice in ["1", "2", "3"]:
    if choice == "1":
      print("\n ---Standard Core Math SUB-INTERFACE---")
      print("   A. Addition (+)")
      print("   B. Subtraction (-)")
      print("   C. Multiplication (*)")
      print("   D. Division (/)")
      sub_choice = input("Select core operation (A-D):").strip().upper()
      if sub_choice in ["A", "B", "C", "D"]:
       try:
        val1 = float(input("Enter initial system parameter (Num 1): "))
        val2 = float(input("Enter Secondary System Modifier (Num2): "))
       except ValueError:
        print(" CRITICAL ERROR: Non_numeric input intercepted. Resetting cycle.")
        continue
       if sub_choice == "A":
        result = add(val1, val2)
        op_name = "Addition"
        equation = f"{val1} + {val2}"
       elif sub_choice == "B":
        result = subtract(val1, val2)
        op_name = "Subtraction"
        equation = f"{val1} - {val2}"
       elif sub_choice == "C":
        result = multiply(val1, val2)
        op_name = "Multiplication"
        equation = f"{val1} * {val2}"
       elif sub_choice == "D":
        result = divide(val1, val2)
        op_name = "Division"
        equation = f"{val1} / {val2}"
       print(f" Sub_Engine Yield: Result = {result}")
       if result == "Error (Div By Zero)":
        print(" Database entry skipped due to illegal system computation.")
       else:
        log_packet = [op_name, equation, result]
        master_session_logs.append(log_packet)
        print(" Data frame securely committed to central RAM storage.")
    elif choice == "3":
      try:
       val1 = float(input("Enter initial system parameter (Num 1): "))
       val2 = float(input("Enter Secondary System Modifier (Num2): "))
      except ValueError:
       print(" CRITICAL ERROR: Non_numeric input intercepted. Resetting cycle.")
       continue
      result = calculate_triangle_area(val1, val2)
      op_name = "Area"
      equation = f"{0.5} * {val1} * {val2}"
      print(f" Core Yield: Area  of Triangle with base {val1} and height {val2} = {result}")
      log_packet = [op_name, equation, result]
      master_session_logs.append(log_packet)
      print(" Data frame securely committed to central RAM storage.")
    elif choice == "2":
      print("\n  --- ADVANCED OPERATION SUB-INTERFACE ---")
      print("  A. Exponent Power Routine (X^Y)")
      print("  B. Percentage Scaling Routine (%)")
      sub_choice = input("Select Advanced Operation (A-B): ").strip().upper()
      if sub_choice in ["A", "B"]:
        try:
         val1 = float(input("Enter initial system parameter (Num 1): "))
         val2 = float(input("Enter Secondary System Modifier (Num2): "))
        except ValueError:
         print(" CRITICAL ERROR: Non_numeric input intercepted. Resetting cycle.")
         continue
        if sub_choice == "A":
          result = calculate_power(val1, val2)
          op_name = "Exponent"
          equation = f"{val1} ** {val2}"
        elif sub_choice =="B":
          result = calculate_percentage(val1, val2)
          op_name = "Percentage"
          equation = f"{val2}% of {val1}"
        print(f" Sub_Engine Yield: Result = {result}")
        if result == "Error (Div By Zero)":
         print(" Database entry skipped due to illegal system computation.")
        else:
         log_packet = [op_name, equation, result]
         master_session_logs.append(log_packet)
         print(" Data frame securely committed to central RAM storage.")
  else:
    print(" Action vector rejected. Selected index sits outside system protocols.")
