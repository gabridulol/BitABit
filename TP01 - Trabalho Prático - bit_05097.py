# Trabalho Prático 01
# Lógica e Operações Bit a Bit
# Gabriel Rodrigues Marques - 05097



cont = 0
s3 = []
s4 = []
n = int(input())
s1 = list(map(str, input().strip()))
s2 = list(map(str, input().strip()))
op = list(map(str, input().strip().split(" ")))
if n > 1000:
  print("ERRO")
else:
  if (len(s1) != n):
    print("ERRO")
  else:
    if (len(s2) != n):
      print("ERRO")
    else:
      if len(op) == 3:
        if ((op[1] != "AND") and (op[1] != "OR") and (op[1] != "XOR") and (op[1] != "NAND") and (op[1] != "NOR") and (op[1] != "MOR")):
          print("ERRO")
        else:
          for i in range(n):
            if (s1[i] != "0" and s1[i] != "1") or (s2[i] != "0" and s2[i] != "1"):
              cont = cont + 1
          if cont > 0:
            print("ERRO")
          else:
            if (op[0] == "S1" and op[2] == "S1"):
              if (op[1] == "AND"):
                for i in range(n):
                  if (s1[i] == "0" and s1[i] == "0"):
                    s3.append("0")
                  if (s1[i] == "0" and s1[i] == "1"):
                    s3.append("0")
                  if (s1[i] == "1" and s1[i] == "0"):
                    s3.append("0")
                  if (s1[i] == "1" and s1[i] == "1"):
                    s3.append("1")
                for i in range(n):
                  print(s3[i], end="")
              if (op[1] == "OR"):
                for i in range(n):
                  if (s1[i] == "0" and s1[i] == "0"):
                    s3.append("0")
                  if (s1[i] == "0" and s1[i] == "1"):
                    s3.append("1")
                  if (s1[i] == "1" and s1[i] == "0"):
                    s3.append("1")
                  if (s1[i] == "1" and s1[i] == "1"):
                    s3.append("1")
                for i in range(n):
                  print(s3[i], end="")
              if (op[1] == "XOR"):
                for i in range(n):
                  if (s1[i] == "0" and s1[i] == "0"):
                    s3.append("0")
                  if (s1[i] == "0" and s1[i] == "1"):
                    s3.append("1")
                  if (s1[i] == "1" and s1[i] == "0"):
                    s3.append("1")
                  if (s1[i] == "1" and s1[i] == "1"):
                    s3.append("0")
                for i in range(n):
                  print(s3[i], end="")
              if (op[1] == "NAND"):
                for i in range(n):
                  if (s1[i] == "0" and s1[i] == "0"):
                    s3.append("1")
                  if (s1[i] == "0" and s1[i] == "1"):
                    s3.append("1")
                  if (s1[i] == "1" and s1[i] == "0"):
                    s3.append("1")
                  if (s1[i] == "1" and s1[i] == "1"):
                    s3.append("0")
                for i in range(n):
                  print(s3[i], end="")
              if (op[1] == "NOR"):
                for i in range(n):
                  if (s1[i] == "0" and s1[i] == "0"):
                    s3.append("1")
                  if (s1[i] == "0" and s1[i] == "1"):
                    s3.append("0")
                  if (s1[i] == "1" and s1[i] == "0"):
                    s3.append("0")
                  if (s1[i] == "1" and s1[i] == "1"):
                    s3.append("0")
                for i in range(n):
                  print(s3[i], end="")
              if (op[1] == "MOR"):
                for i in range(n):
                  if (s1[i] == "0" and s1[i] == "0"):
                    s3.append("1")
                  if (s1[i] == "0" and s1[i] == "1"):
                    s3.append("1")
                  if (s1[i] == "1" and s1[i] == "0"):
                    s3.append("0")
                  if (s1[i] == "1" and s1[i] == "1"):
                    s3.append("1")
                for i in range(n):
                  print(s3[i], end="")
            if (op[0] == "S1" and op[2] == "S2"):
              if (op[1] == "AND"):
                for i in range(n):
                  if (s1[i] == "0" and s2[i] == "0"):
                    s3.append("0")
                  if (s1[i] == "0" and s2[i] == "1"):
                    s3.append("0")
                  if (s1[i] == "1" and s2[i] == "0"):
                    s3.append("0")
                  if (s1[i] == "1" and s2[i] == "1"):
                    s3.append("1")
                for i in range(n):
                  print(s3[i], end="")
              if (op[1] == "OR"):
                for i in range(n):
                  if (s1[i] == "0" and s2[i] == "0"):
                    s3.append("0")
                  if (s1[i] == "0" and s2[i] == "1"):
                    s3.append("1")
                  if (s1[i] == "1" and s2[i] == "0"):
                    s3.append("1")
                  if (s1[i] == "1" and s2[i] == "1"):
                    s3.append("1")
                for i in range(n):
                  print(s3[i], end="")
              if (op[1] == "XOR"):
                for i in range(n):
                  if (s1[i] == "0" and s2[i] == "0"):
                    s3.append("0")
                  if (s1[i] == "0" and s2[i] == "1"):
                    s3.append("1")
                  if (s1[i] == "1" and s2[i] == "0"):
                    s3.append("1")
                  if (s1[i] == "1" and s2[i] == "1"):
                    s3.append("0")
                for i in range(n):
                  print(s3[i], end="")
              if (op[1] == "NAND"):
                for i in range(n):
                  if (s1[i] == "0" and s2[i] == "0"):
                    s3.append("1")
                  if (s1[i] == "0" and s2[i] == "1"):
                    s3.append("1")
                  if (s1[i] == "1" and s2[i] == "0"):
                    s3.append("1")
                  if (s1[i] == "1" and s2[i] == "1"):
                    s3.append("0")
                for i in range(n):
                  print(s3[i], end="")
              if (op[1] == "NOR"):
                for i in range(n):
                  if (s1[i] == "0" and s2[i] == "0"):
                    s3.append("1")
                  if (s1[i] == "0" and s2[i] == "1"):
                    s3.append("0")
                  if (s1[i] == "1" and s2[i] == "0"):
                    s3.append("0")
                  if (s1[i] == "1" and s2[i] == "1"):
                    s3.append("0")
                for i in range(n):
                  print(s3[i], end="")
              if (op[1] == "MOR"):
                for i in range(n):
                  if (s1[i] == "0" and s2[i] == "0"):
                    s3.append("1")
                  if (s1[i] == "0" and s2[i] == "1"):
                    s3.append("1")
                  if (s1[i] == "1" and s2[i] == "0"):
                    s3.append("0")
                  if (s1[i] == "1" and s2[i] == "1"):
                    s3.append("1")
                for i in range(n):
                  print(s3[i], end="")
            if (op[0] == "S2" and op[2] == "S1"):
              if (op[1] == "AND"):
                for i in range(n):
                  if (s2[i] == "0" and s1[i] == "0"):
                    s3.append("0")
                  if (s2[i] == "1" and s1[i] == "0"):
                    s3.append("0")
                  if (s2[i] == "0" and s1[i] == "1"):
                    s3.append("0")
                  if (s2[i] == "1" and s1[i] == "1"):
                    s3.append("1")
                for i in range(n):
                  print(s3[i], end="")
              if (op[1] == "OR"):
                for i in range(n):
                  if (s2[i] == "0" and s1[i] == "0"):
                    s3.append("0")
                  if (s2[i] == "1" and s1[i] == "0"):
                    s3.append("1")
                  if (s2[i] == "0" and s1[i] == "1"):
                    s3.append("1")
                  if (s2[i] == "1" and s1[i] == "1"):
                    s3.append("1")
                for i in range(n):
                  print(s3[i], end="")
              if (op[1] == "XOR"):
                for i in range(n):
                  if (s2[i] == "0" and s1[i] == "0"):
                    s3.append("0")
                  if (s2[i] == "1" and s1[i] == "0"):
                    s3.append("1")
                  if (s2[i] == "0" and s1[i] == "1"):
                    s3.append("1")
                  if (s2[i] == "1" and s1[i] == "1"):
                    s3.append("0")
                for i in range(n):
                  print(s3[i], end="")
              if (op[1] == "NAND"):
                for i in range(n):
                  if (s2[i] == "0" and s1[i] == "0"):
                    s3.append("1")
                  if (s2[i] == "1" and s1[i] == "0"):
                    s3.append("1")
                  if (s2[i] == "0" and s1[i] == "1"):
                    s3.append("1")
                  if (s2[i] == "1" and s1[i] == "1"):
                    s3.append("0")
                for i in range(n):
                  print(s3[i], end="")
              if (op[1] == "NOR"):
                for i in range(n):
                  if (s2[i] == "0" and s1[i] == "0"):
                    s3.append("1")
                  if (s2[i] == "1" and s1[i] == "0"):
                    s3.append("0")
                  if (s2[i] == "0" and s1[i] == "1"):
                    s3.append("0")
                  if (s2[i] == "1" and s1[i] == "1"):
                    s3.append("0")
                for i in range(n):
                  print(s3[i], end="")
              if (op[1] == "MOR"):
                for i in range(n):
                  if (s2[i] == "0" and s1[i] == "0"):
                    s3.append("1")
                  if (s2[i] == "1" and s1[i] == "0"):
                    s3.append("0")
                  if (s2[i] == "0" and s1[i] == "1"):
                    s3.append("1")
                  if (s2[i] == "1" and s1[i] == "1"):
                    s3.append("1")
                for i in range(n):
                  print(s3[i], end="")
            if (op[0] == "S2" and op[2] == "S2"):
              if (op[1] == "AND"):
                for i in range(n):
                  if (s2[i] == "0" and s2[i] == "0"):
                    s3.append("0")
                  if (s2[i] == "0" and s2[i] == "1"):
                    s3.append("0")
                  if (s2[i] == "1" and s2[i] == "0"):
                    s3.append("0")
                  if (s2[i] == "1" and s2[i] == "1"):
                    s3.append("1")
                for i in range(n):
                  print(s3[i], end="")
              if (op[1] == "OR"):
                for i in range(n):
                  if (s2[i] == "0" and s2[i] == "0"):
                    s3.append("0")
                  if (s2[i] == "0" and s2[i] == "1"):
                    s3.append("1")
                  if (s2[i] == "1" and s2[i] == "0"):
                    s3.append("1")
                  if (s2[i] == "1" and s2[i] == "1"):
                    s3.append("1")
                for i in range(n):
                  print(s3[i], end="")
              if (op[1] == "XOR"):
                for i in range(n):
                  if (s2[i] == "0" and s2[i] == "0"):
                    s3.append("0")
                  if (s2[i] == "0" and s2[i] == "1"):
                    s3.append("1")
                  if (s2[i] == "1" and s2[i] == "0"):
                    s3.append("1")
                  if (s2[i] == "1" and s2[i] == "1"):
                    s3.append("0")
                for i in range(n):
                  print(s3[i], end="")
              if (op[1] == "NAND"):
                for i in range(n):
                  if (s2[i] == "0" and s2[i] == "0"):
                    s3.append("1")
                  if (s2[i] == "0" and s2[i] == "1"):
                    s3.append("1")
                  if (s2[i] == "1" and s2[i] == "0"):
                    s3.append("1")
                  if (s2[i] == "1" and s2[i] == "1"):
                    s3.append("0")
                for i in range(n):
                  print(s3[i], end="")
              if (op[1] == "NOR"):
                for i in range(n):
                  if (s2[i] == "0" and s2[i] == "0"):
                    s3.append("1")
                  if (s2[i] == "0" and s2[i] == "1"):
                    s3.append("0")
                  if (s2[i] == "1" and s2[i] == "0"):
                    s3.append("0")
                  if (s2[i] == "1" and s2[i] == "1"):
                    s3.append("0")
                for i in range(n):
                  print(s3[i], end="")
              if (op[1] == "MOR"):
                for i in range(n):
                  if (s2[i] == "0" and s2[i] == "0"):
                    s3.append("1")
                  if (s2[i] == "0" and s2[i] == "1"):
                    s3.append("1")
                  if (s2[i] == "1" and s2[i] == "0"):
                    s3.append("0")
                  if (s2[i] == "1" and s2[i] == "1"):
                    s3.append("1")
                for i in range(n):
                  print(s3[i], end="")
      if len(op) == 5:
        if ((op[1] != "AND") and (op[1] != "OR") and (op[1] != "XOR") and (op[1] != "NAND") and (op[1] != "NOR") and (op[1] != "MOR")):
          print("ERRO")
        else:
          if ((op[3] != "AND") and (op[3] != "OR") and (op[3] != "XOR") and (op[3] != "NAND") and (op[3] != "NOR") and (op[3] != "MOR")):
            print("ERRO")
          else:
            for i in range(n):
              if (s1[i] != "0" and s1[i] != "1") or (s2[i] != "0" and s2[i] != "1"):
                cont = cont + 1
            if cont > 0:
              print("ERRO")
            else:
              if (op[0] == "S1" and op[2] == "S1"):
                if (op[1] == "AND"):
                  for i in range(n):
                    if (s1[i] == "0" and s1[i] == "0"):
                      s3.append("0")
                    if (s1[i] == "0" and s1[i] == "1"):
                      s3.append("0")
                    if (s1[i] == "1" and s1[i] == "0"):
                      s3.append("0")
                    if (s1[i] == "1" and s1[i] == "1"):
                      s3.append("1")
                if (op[1] == "OR"):
                  for i in range(n):
                    if (s1[i] == "0" and s1[i] == "0"):
                      s3.append("0")
                    if (s1[i] == "0" and s1[i] == "1"):
                      s3.append("1")
                    if (s1[i] == "1" and s1[i] == "0"):
                      s3.append("1")
                    if (s1[i] == "1" and s1[i] == "1"):
                      s3.append("1")
                if (op[1] == "XOR"):
                  for i in range(n):
                    if (s1[i] == "0" and s1[i] == "0"):
                      s3.append("0")
                    if (s1[i] == "0" and s1[i] == "1"):
                      s3.append("1")
                    if (s1[i] == "1" and s1[i] == "0"):
                      s3.append("1")
                    if (s1[i] == "1" and s1[i] == "1"):
                      s3.append("0")
                if (op[1] == "NAND"):
                  for i in range(n):
                    if (s1[i] == "0" and s1[i] == "0"):
                      s3.append("1")
                    if (s1[i] == "0" and s1[i] == "1"):
                      s3.append("1")
                    if (s1[i] == "1" and s1[i] == "0"):
                      s3.append("1")
                    if (s1[i] == "1" and s1[i] == "1"):
                      s3.append("0")
                if (op[1] == "NOR"):
                  for i in range(n):
                    if (s1[i] == "0" and s1[i] == "0"):
                      s3.append("1")
                    if (s1[i] == "0" and s1[i] == "1"):
                      s3.append("0")
                    if (s1[i] == "1" and s1[i] == "0"):
                      s3.append("0")
                    if (s1[i] == "1" and s1[i] == "1"):
                      s3.append("0")
                if (op[1] == "MOR"):
                  for i in range(n):
                    if (s1[i] == "0" and s1[i] == "0"):
                      s3.append("1")
                    if (s1[i] == "0" and s1[i] == "1"):
                      s3.append("1")
                    if (s1[i] == "1" and s1[i] == "0"):
                      s3.append("0")
                    if (s1[i] == "1" and s1[i] == "1"):
                      s3.append("1")
                if (op[4] == "S1"):
                  if (op[3] == "AND"):
                    for i in range(n):
                      if (s3[i] == "0" and s1[i] == "0"):
                        s4.append("0")
                      if (s3[i] == "0" and s1[i] == "1"):
                        s4.append("0")
                      if (s3[i] == "1" and s1[i] == "0"):
                        s4.append("0")
                      if (s3[i] == "1" and s1[i] == "1"):
                        s4.append("1")
                    for i in range(n):
                      print(s4[i], end="")
                  if (op[3] == "OR"):
                    for i in range(n):
                      if (s3[i] == "0" and s1[i] == "0"):
                        s4.append("0")
                      if (s3[i] == "0" and s1[i] == "1"):
                        s4.append("1")
                      if (s3[i] == "1" and s1[i] == "0"):
                        s4.append("1")
                      if (s3[i] == "1" and s1[i] == "1"):
                        s4.append("1")
                    for i in range(n):
                      print(s4[i], end="")
                  if (op[3] == "XOR"):
                    for i in range(n):
                      if (s3[i] == "0" and s1[i] == "0"):
                        s4.append("0")
                      if (s3[i] == "0" and s1[i] == "1"):
                        s4.append("1")
                      if (s3[i] == "1" and s1[i] == "0"):
                        s4.append("1")
                      if (s3[i] == "1" and s1[i] == "1"):
                        s4.append("0")
                    for i in range(n):
                      print(s4[i], end="")
                  if (op[3] == "NAND"):
                    for i in range(n):
                      if (s3[i] == "0" and s1[i] == "0"):
                        s4.append("1")
                      if (s3[i] == "0" and s1[i] == "1"):
                        s4.append("1")
                      if (s3[i] == "1" and s1[i] == "0"):
                        s4.append("1")
                      if (s3[i] == "1" and s1[i] == "1"):
                        s4.append("0")
                    for i in range(n):
                      print(s4[i], end="")
                  if (op[3] == "NOR"):
                    for i in range(n):
                      if (s3[i] == "0" and s1[i] == "0"):
                        s4.append("1")
                      if (s3[i] == "0" and s1[i] == "1"):
                        s4.append("0")
                      if (s3[i] == "1" and s1[i] == "0"):
                        s4.append("0")
                      if (s3[i] == "1" and s1[i] == "1"):
                        s4.append("0")
                    for i in range(n):
                      print(s4[i], end="")
                  if (op[3] == "MOR"):
                    for i in range(n):
                      if (s3[i] == "0" and s1[i] == "0"):
                        s4.append("1")
                      if (s3[i] == "0" and s1[i] == "1"):
                        s4.append("1")
                      if (s3[i] == "1" and s1[i] == "0"):
                        s4.append("0")
                      if (s3[i] == "1" and s1[i] == "1"):
                        s4.append("1")
                    for i in range(n):
                      print(s4[i], end="")
                if (op[4] == "S2"):
                  if (op[3] == "AND"):
                    for i in range(n):
                      if (s3[i] == "0" and s2[i] == "0"):
                        s4.append("0")
                      if (s3[i] == "0" and s2[i] == "1"):
                        s4.append("0")
                      if (s3[i] == "1" and s2[i] == "0"):
                        s4.append("0")
                      if (s3[i] == "1" and s2[i] == "1"):
                        s4.append("1")
                    for i in range(n):
                      print(s4[i], end="")
                  if (op[3] == "OR"):
                    for i in range(n):
                      if (s3[i] == "0" and s2[i] == "0"):
                        s4.append("0")
                      if (s3[i] == "0" and s2[i] == "1"):
                        s4.append("1")
                      if (s3[i] == "1" and s2[i] == "0"):
                        s4.append("1")
                      if (s3[i] == "1" and s2[i] == "1"):
                        s4.append("1")
                    for i in range(n):
                      print(s4[i], end="")
                  if (op[3] == "XOR"):
                    for i in range(n):
                      if (s3[i] == "0" and s2[i] == "0"):
                        s4.append("0")
                      if (s3[i] == "0" and s2[i] == "1"):
                        s4.append("1")
                      if (s3[i] == "1" and s2[i] == "0"):
                        s4.append("1")
                      if (s3[i] == "1" and s2[i] == "1"):
                        s4.append("0")
                    for i in range(n):
                      print(s4[i], end="")
                  if (op[3] == "NAND"):
                    for i in range(n):
                      if (s3[i] == "0" and s2[i] == "0"):
                        s4.append("1")
                      if (s3[i] == "0" and s2[i] == "1"):
                        s4.append("1")
                      if (s3[i] == "1" and s2[i] == "0"):
                        s4.append("1")
                      if (s3[i] == "1" and s2[i] == "1"):
                        s4.append("0")
                    for i in range(n):
                      print(s4[i], end="")
                  if (op[3] == "NOR"):
                    for i in range(n):
                      if (s3[i] == "0" and s2[i] == "0"):
                        s4.append("1")
                      if (s3[i] == "0" and s2[i] == "1"):
                        s4.append("0")
                      if (s3[i] == "1" and s2[i] == "0"):
                        s4.append("0")
                      if (s3[i] == "1" and s2[i] == "1"):
                        s4.append("0")
                    for i in range(n):
                      print(s4[i], end="")
                  if (op[3] == "MOR"):
                    for i in range(n):
                      if (s3[i] == "0" and s2[i] == "0"):
                        s4.append("1")
                      if (s3[i] == "0" and s2[i] == "1"):
                        s4.append("1")
                      if (s3[i] == "1" and s2[i] == "0"):
                        s4.append("0")
                      if (s3[i] == "1" and s2[i] == "1"):
                        s4.append("1")
                    for i in range(n):
                      print(s4[i], end="")
              if (op[0] == "S1" and op[2] == "S2"):
                if (op[1] == "AND"):
                  for i in range(n):
                    if (s1[i] == "0" and s2[i] == "0"):
                      s3.append("0")
                    if (s1[i] == "0" and s2[i] == "1"):
                      s3.append("0")
                    if (s1[i] == "1" and s2[i] == "0"):
                      s3.append("0")
                    if (s1[i] == "1" and s2[i] == "1"):
                      s3.append("1")
                if (op[1] == "OR"):
                  for i in range(n):
                    if (s1[i] == "0" and s2[i] == "0"):
                      s3.append("0")
                    if (s1[i] == "0" and s2[i] == "1"):
                      s3.append("1")
                    if (s1[i] == "1" and s2[i] == "0"):
                      s3.append("1")
                    if (s1[i] == "1" and s2[i] == "1"):
                      s3.append("1")
                if (op[1] == "XOR"):
                  for i in range(n):
                    if (s1[i] == "0" and s2[i] == "0"):
                      s3.append("0")
                    if (s1[i] == "0" and s2[i] == "1"):
                      s3.append("1")
                    if (s1[i] == "1" and s2[i] == "0"):
                      s3.append("1")
                    if (s1[i] == "1" and s2[i] == "1"):
                      s3.append("0")
                if (op[1] == "NAND"):
                  for i in range(n):
                    if (s1[i] == "0" and s2[i] == "0"):
                      s3.append("1")
                    if (s1[i] == "0" and s2[i] == "1"):
                      s3.append("1")
                    if (s1[i] == "1" and s2[i] == "0"):
                      s3.append("1")
                    if (s1[i] == "1" and s2[i] == "1"):
                      s3.append("0")
                if (op[1] == "NOR"):
                  for i in range(n):
                    if (s1[i] == "0" and s2[i] == "0"):
                      s3.append("1")
                    if (s1[i] == "0" and s2[i] == "1"):
                      s3.append("0")
                    if (s1[i] == "1" and s2[i] == "0"):
                      s3.append("0")
                    if (s1[i] == "1" and s2[i] == "1"):
                      s3.append("0")
                if (op[1] == "MOR"):
                  for i in range(n):
                    if (s1[i] == "0" and s2[i] == "0"):
                      s3.append("1")
                    if (s1[i] == "0" and s2[i] == "1"):
                      s3.append("1")
                    if (s1[i] == "1" and s2[i] == "0"):
                      s3.append("0")
                    if (s1[i] == "1" and s2[i] == "1"):
                      s3.append("1")
                if (op[4] == "S1"):
                  if (op[3] == "AND"):
                    for i in range(n):
                      if (s3[i] == "0" and s1[i] == "0"):
                        s4.append("0")
                      if (s3[i] == "0" and s1[i] == "1"):
                        s4.append("0")
                      if (s3[i] == "1" and s1[i] == "0"):
                        s4.append("0")
                      if (s3[i] == "1" and s1[i] == "1"):
                        s4.append("1")
                    for i in range(n):
                      print(s4[i], end="")
                  if (op[3] == "OR"):
                    for i in range(n):
                      if (s3[i] == "0" and s1[i] == "0"):
                        s4.append("0")
                      if (s3[i] == "0" and s1[i] == "1"):
                        s4.append("1")
                      if (s3[i] == "1" and s1[i] == "0"):
                        s4.append("1")
                      if (s3[i] == "1" and s1[i] == "1"):
                        s4.append("1")
                    for i in range(n):
                      print(s4[i], end="")
                  if (op[3] == "XOR"):
                    for i in range(n):
                      if (s3[i] == "0" and s1[i] == "0"):
                        s4.append("0")
                      if (s3[i] == "0" and s1[i] == "1"):
                        s4.append("1")
                      if (s3[i] == "1" and s1[i] == "0"):
                        s4.append("1")
                      if (s3[i] == "1" and s1[i] == "1"):
                        s4.append("0")
                    for i in range(n):
                      print(s4[i], end="")
                  if (op[3] == "NAND"):
                    for i in range(n):
                      if (s3[i] == "0" and s1[i] == "0"):
                        s4.append("1")
                      if (s3[i] == "0" and s1[i] == "1"):
                        s4.append("1")
                      if (s3[i] == "1" and s1[i] == "0"):
                        s4.append("1")
                      if (s3[i] == "1" and s1[i] == "1"):
                        s4.append("0")
                    for i in range(n):
                      print(s4[i], end="")
                  if (op[3] == "NOR"):
                    for i in range(n):
                      if (s3[i] == "0" and s1[i] == "0"):
                        s4.append("1")
                      if (s3[i] == "0" and s1[i] == "1"):
                        s4.append("0")
                      if (s3[i] == "1" and s1[i] == "0"):
                        s4.append("0")
                      if (s3[i] == "1" and s1[i] == "1"):
                        s4.append("0")
                    for i in range(n):
                      print(s4[i], end="")
                  if (op[3] == "MOR"):
                    for i in range(n):
                      if (s3[i] == "0" and s1[i] == "0"):
                        s4.append("1")
                      if (s3[i] == "0" and s1[i] == "1"):
                        s4.append("1")
                      if (s3[i] == "1" and s1[i] == "0"):
                        s4.append("0")
                      if (s3[i] == "1" and s1[i] == "1"):
                        s4.append("1")
                    for i in range(n):
                      print(s4[i], end="")
                if (op[4] == "S2"):
                  if (op[3] == "AND"):
                    for i in range(n):
                      if (s3[i] == "0" and s2[i] == "0"):
                        s4.append("0")
                      if (s3[i] == "0" and s2[i] == "1"):
                        s4.append("0")
                      if (s3[i] == "1" and s2[i] == "0"):
                        s4.append("0")
                      if (s3[i] == "1" and s2[i] == "1"):
                        s4.append("1")
                    for i in range(n):
                      print(s4[i], end="")
                  if (op[3] == "OR"):
                    for i in range(n):
                      if (s3[i] == "0" and s2[i] == "0"):
                        s4.append("0")
                      if (s3[i] == "0" and s2[i] == "1"):
                        s4.append("1")
                      if (s3[i] == "1" and s2[i] == "0"):
                        s4.append("1")
                      if (s3[i] == "1" and s2[i] == "1"):
                        s4.append("1")
                    for i in range(n):
                      print(s4[i], end="")
                  if (op[3] == "XOR"):
                    for i in range(n):
                      if (s3[i] == "0" and s2[i] == "0"):
                        s4.append("0")
                      if (s3[i] == "0" and s2[i] == "1"):
                        s4.append("1")
                      if (s3[i] == "1" and s2[i] == "0"):
                        s4.append("1")
                      if (s3[i] == "1" and s2[i] == "1"):
                        s4.append("0")
                    for i in range(n):
                      print(s4[i], end="")
                  if (op[3] == "NAND"):
                    for i in range(n):
                      if (s3[i] == "0" and s2[i] == "0"):
                        s4.append("1")
                      if (s3[i] == "0" and s2[i] == "1"):
                        s4.append("1")
                      if (s3[i] == "1" and s2[i] == "0"):
                        s4.append("1")
                      if (s3[i] == "1" and s2[i] == "1"):
                        s4.append("0")
                    for i in range(n):
                      print(s4[i], end="")
                  if (op[3] == "NOR"):
                    for i in range(n):
                      if (s3[i] == "0" and s2[i] == "0"):
                        s4.append("1")
                      if (s3[i] == "0" and s2[i] == "1"):
                        s4.append("0")
                      if (s3[i] == "1" and s2[i] == "0"):
                        s4.append("0")
                      if (s3[i] == "1" and s2[i] == "1"):
                        s4.append("0")
                    for i in range(n):
                      print(s4[i], end="")
                  if (op[3] == "MOR"):
                    for i in range(n):
                      if (s3[i] == "0" and s2[i] == "0"):
                        s4.append("1")
                      if (s3[i] == "0" and s2[i] == "1"):
                        s4.append("1")
                      if (s3[i] == "1" and s2[i] == "0"):
                        s4.append("0")
                      if (s3[i] == "1" and s2[i] == "1"):
                        s4.append("1")
                    for i in range(n):
                      print(s4[i], end="")
              if (op[0] == "S2" and op[2] == "S1"):
                if (op[1] == "AND"):
                  for i in range(n):
                    if (s2[i] == "0" and s1[i] == "0"):
                      s3.append("0")
                    if (s2[i] == "1" and s1[i] == "0"):
                      s3.append("0")
                    if (s2[i] == "0" and s1[i] == "1"):
                      s3.append("0")
                    if (s2[i] == "1" and s1[i] == "1"):
                      s3.append("1")
                if (op[1] == "OR"):
                  for i in range(n):
                    if (s2[i] == "0" and s1[i] == "0"):
                      s3.append("0")
                    if (s2[i] == "1" and s1[i] == "0"):
                      s3.append("1")
                    if (s2[i] == "0" and s1[i] == "1"):
                      s3.append("1")
                    if (s2[i] == "1" and s1[i] == "1"):
                      s3.append("1")
                if (op[1] == "XOR"):
                  for i in range(n):
                    if (s2[i] == "0" and s1[i] == "0"):
                      s3.append("0")
                    if (s2[i] == "1" and s1[i] == "0"):
                      s3.append("1")
                    if (s2[i] == "0" and s1[i] == "1"):
                      s3.append("1")
                    if (s2[i] == "1" and s1[i] == "1"):
                      s3.append("0")
                if (op[1] == "NAND"):
                  for i in range(n):
                    if (s2[i] == "0" and s1[i] == "0"):
                      s3.append("1")
                    if (s2[i] == "1" and s1[i] == "0"):
                      s3.append("1")
                    if (s2[i] == "0" and s1[i] == "1"):
                      s3.append("1")
                    if (s2[i] == "1" and s1[i] == "1"):
                      s3.append("0")
                if (op[1] == "NOR"):
                  for i in range(n):
                    if (s2[i] == "0" and s1[i] == "0"):
                      s3.append("1")
                    if (s2[i] == "1" and s1[i] == "0"):
                      s3.append("0")
                    if (s2[i] == "0" and s1[i] == "1"):
                      s3.append("0")
                    if (s2[i] == "1" and s1[i] == "1"):
                      s3.append("0")
                if (op[1] == "MOR"):
                  for i in range(n):
                    if (s2[i] == "0" and s1[i] == "0"):
                      s3.append("1")
                    if (s2[i] == "1" and s1[i] == "0"):
                      s3.append("0")
                    if (s2[i] == "0" and s1[i] == "1"):
                      s3.append("1")
                    if (s2[i] == "1" and s1[i] == "1"):
                      s3.append("1")
                if (op[4] == "S1"):
                  if (op[3] == "AND"):
                    for i in range(n):
                      if (s3[i] == "0" and s1[i] == "0"):
                        s4.append("0")
                      if (s3[i] == "0" and s1[i] == "1"):
                        s4.append("0")
                      if (s3[i] == "1" and s1[i] == "0"):
                        s4.append("0")
                      if (s3[i] == "1" and s1[i] == "1"):
                        s4.append("1")
                    for i in range(n):
                      print(s4[i], end="")
                  if (op[3] == "OR"):
                    for i in range(n):
                      if (s3[i] == "0" and s1[i] == "0"):
                        s4.append("0")
                      if (s3[i] == "0" and s1[i] == "1"):
                        s4.append("1")
                      if (s3[i] == "1" and s1[i] == "0"):
                        s4.append("1")
                      if (s3[i] == "1" and s1[i] == "1"):
                        s4.append("1")
                    for i in range(n):
                      print(s4[i], end="")
                  if (op[3] == "XOR"):
                    for i in range(n):
                      if (s3[i] == "0" and s1[i] == "0"):
                        s4.append("0")
                      if (s3[i] == "0" and s1[i] == "1"):
                        s4.append("1")
                      if (s3[i] == "1" and s1[i] == "0"):
                        s4.append("1")
                      if (s3[i] == "1" and s1[i] == "1"):
                        s4.append("0")
                    for i in range(n):
                      print(s4[i], end="")
                  if (op[3] == "NAND"):
                    for i in range(n):
                      if (s3[i] == "0" and s1[i] == "0"):
                        s4.append("1")
                      if (s3[i] == "0" and s1[i] == "1"):
                        s4.append("1")
                      if (s3[i] == "1" and s1[i] == "0"):
                        s4.append("1")
                      if (s3[i] == "1" and s1[i] == "1"):
                        s4.append("0")
                    for i in range(n):
                      print(s4[i], end="")
                  if (op[3] == "NOR"):
                    for i in range(n):
                      if (s3[i] == "0" and s1[i] == "0"):
                        s4.append("1")
                      if (s3[i] == "0" and s1[i] == "1"):
                        s4.append("0")
                      if (s3[i] == "1" and s1[i] == "0"):
                        s4.append("0")
                      if (s3[i] == "1" and s1[i] == "1"):
                        s4.append("0")
                    for i in range(n):
                      print(s4[i], end="")
                  if (op[3] == "MOR"):
                    for i in range(n):
                      if (s3[i] == "0" and s1[i] == "0"):
                        s4.append("1")
                      if (s3[i] == "0" and s1[i] == "1"):
                        s4.append("1")
                      if (s3[i] == "1" and s1[i] == "0"):
                        s4.append("0")
                      if (s3[i] == "1" and s1[i] == "1"):
                        s4.append("1")
                    for i in range(n):
                      print(s4[i], end="")
                if (op[4] == "S2"):
                  if (op[3] == "AND"):
                    for i in range(n):
                      if (s3[i] == "0" and s2[i] == "0"):
                        s4.append("0")
                      if (s3[i] == "0" and s2[i] == "1"):
                        s4.append("0")
                      if (s3[i] == "1" and s2[i] == "0"):
                        s4.append("0")
                      if (s3[i] == "1" and s2[i] == "1"):
                        s4.append("1")
                    for i in range(n):
                      print(s4[i], end="")
                  if (op[3] == "OR"):
                    for i in range(n):
                      if (s3[i] == "0" and s2[i] == "0"):
                        s4.append("0")
                      if (s3[i] == "0" and s2[i] == "1"):
                        s4.append("1")
                      if (s3[i] == "1" and s2[i] == "0"):
                        s4.append("1")
                      if (s3[i] == "1" and s2[i] == "1"):
                        s4.append("1")
                    for i in range(n):
                      print(s4[i], end="")
                  if (op[3] == "XOR"):
                    for i in range(n):
                      if (s3[i] == "0" and s2[i] == "0"):
                        s4.append("0")
                      if (s3[i] == "0" and s2[i] == "1"):
                        s4.append("1")
                      if (s3[i] == "1" and s2[i] == "0"):
                        s4.append("1")
                      if (s3[i] == "1" and s2[i] == "1"):
                        s4.append("0")
                    for i in range(n):
                      print(s4[i], end="")
                  if (op[3] == "NAND"):
                    for i in range(n):
                      if (s3[i] == "0" and s2[i] == "0"):
                        s4.append("1")
                      if (s3[i] == "0" and s2[i] == "1"):
                        s4.append("1")
                      if (s3[i] == "1" and s2[i] == "0"):
                        s4.append("1")
                      if (s3[i] == "1" and s2[i] == "1"):
                        s4.append("0")
                    for i in range(n):
                      print(s4[i], end="")
                  if (op[3] == "NOR"):
                    for i in range(n):
                      if (s3[i] == "0" and s2[i] == "0"):
                        s4.append("1")
                      if (s3[i] == "0" and s2[i] == "1"):
                        s4.append("0")
                      if (s3[i] == "1" and s2[i] == "0"):
                        s4.append("0")
                      if (s3[i] == "1" and s2[i] == "1"):
                        s4.append("0")
                    for i in range(n):
                      print(s4[i], end="")
                  if (op[3] == "MOR"):
                    for i in range(n):
                      if (s3[i] == "0" and s2[i] == "0"):
                        s4.append("1")
                      if (s3[i] == "0" and s2[i] == "1"):
                        s4.append("1")
                      if (s3[i] == "1" and s2[i] == "0"):
                        s4.append("0")
                      if (s3[i] == "1" and s2[i] == "1"):
                        s4.append("1")
                    for i in range(n):
                      print(s4[i], end="")
              if (op[0] == "S2" and op[2] == "S2"):
                if (op[1] == "AND"):
                  for i in range(n):
                    if (s2[i] == "0" and s2[i] == "0"):
                      s3.append("0")
                    if (s2[i] == "0" and s2[i] == "1"):
                      s3.append("0")
                    if (s2[i] == "1" and s2[i] == "0"):
                      s3.append("0")
                    if (s2[i] == "1" and s2[i] == "1"):
                      s3.append("1")
                if (op[1] == "OR"):
                  for i in range(n):
                    if (s2[i] == "0" and s2[i] == "0"):
                      s3.append("0")
                    if (s2[i] == "0" and s2[i] == "1"):
                      s3.append("1")
                    if (s2[i] == "1" and s2[i] == "0"):
                      s3.append("1")
                    if (s2[i] == "1" and s2[i] == "1"):
                      s3.append("1")
                if (op[1] == "XOR"):
                  for i in range(n):
                    if (s2[i] == "0" and s2[i] == "0"):
                      s3.append("0")
                    if (s2[i] == "0" and s2[i] == "1"):
                      s3.append("1")
                    if (s2[i] == "1" and s2[i] == "0"):
                      s3.append("1")
                    if (s2[i] == "1" and s2[i] == "1"):
                      s3.append("0")
                if (op[1] == "NAND"):
                  for i in range(n):
                    if (s2[i] == "0" and s2[i] == "0"):
                      s3.append("1")
                    if (s2[i] == "0" and s2[i] == "1"):
                      s3.append("1")
                    if (s2[i] == "1" and s2[i] == "0"):
                      s3.append("1")
                    if (s2[i] == "1" and s2[i] == "1"):
                      s3.append("0")
                if (op[1] == "NOR"):
                  for i in range(n):
                    if (s2[i] == "0" and s2[i] == "0"):
                      s3.append("1")
                    if (s2[i] == "0" and s2[i] == "1"):
                      s3.append("0")
                    if (s2[i] == "1" and s2[i] == "0"):
                      s3.append("0")
                    if (s2[i] == "1" and s2[i] == "1"):
                      s3.append("0")
                if (op[1] == "MOR"):
                  for i in range(n):
                    if (s2[i] == "0" and s2[i] == "0"):
                      s3.append("1")
                    if (s2[i] == "0" and s2[i] == "1"):
                      s3.append("1")
                    if (s2[i] == "1" and s2[i] == "0"):
                      s3.append("0")
                    if (s2[i] == "1" and s2[i] == "1"):
                      s3.append("1")
                if (op[4] == "S1"):
                  if (op[3] == "AND"):
                    for i in range(n):
                      if (s3[i] == "0" and s1[i] == "0"):
                        s4.append("0")
                      if (s3[i] == "0" and s1[i] == "1"):
                        s4.append("0")
                      if (s3[i] == "1" and s1[i] == "0"):
                        s4.append("0")
                      if (s3[i] == "1" and s1[i] == "1"):
                        s4.append("1")
                    for i in range(n):
                      print(s4[i], end="")
                  if (op[3] == "OR"):
                    for i in range(n):
                      if (s3[i] == "0" and s1[i] == "0"):
                        s4.append("0")
                      if (s3[i] == "0" and s1[i] == "1"):
                        s4.append("1")
                      if (s3[i] == "1" and s1[i] == "0"):
                        s4.append("1")
                      if (s3[i] == "1" and s1[i] == "1"):
                        s4.append("1")
                    for i in range(n):
                      print(s4[i], end="")
                  if (op[3] == "XOR"):
                    for i in range(n):
                      if (s3[i] == "0" and s1[i] == "0"):
                        s4.append("0")
                      if (s3[i] == "0" and s1[i] == "1"):
                        s4.append("1")
                      if (s3[i] == "1" and s1[i] == "0"):
                        s4.append("1")
                      if (s3[i] == "1" and s1[i] == "1"):
                        s4.append("0")
                    for i in range(n):
                      print(s4[i], end="")
                  if (op[3] == "NAND"):
                    for i in range(n):
                      if (s3[i] == "0" and s1[i] == "0"):
                        s4.append("1")
                      if (s3[i] == "0" and s1[i] == "1"):
                        s4.append("1")
                      if (s3[i] == "1" and s1[i] == "0"):
                        s4.append("1")
                      if (s3[i] == "1" and s1[i] == "1"):
                        s4.append("0")
                    for i in range(n):
                      print(s4[i], end="")
                  if (op[3] == "NOR"):
                    for i in range(n):
                      if (s3[i] == "0" and s1[i] == "0"):
                        s4.append("1")
                      if (s3[i] == "0" and s1[i] == "1"):
                        s4.append("0")
                      if (s3[i] == "1" and s1[i] == "0"):
                        s4.append("0")
                      if (s3[i] == "1" and s1[i] == "1"):
                        s4.append("0")
                    for i in range(n):
                      print(s4[i], end="")
                  if (op[3] == "MOR"):
                    for i in range(n):
                      if (s3[i] == "0" and s1[i] == "0"):
                        s4.append("1")
                      if (s3[i] == "0" and s1[i] == "1"):
                        s4.append("1")
                      if (s3[i] == "1" and s1[i] == "0"):
                        s4.append("0")
                      if (s3[i] == "1" and s1[i] == "1"):
                        s4.append("1")
                    for i in range(n):
                      print(s4[i], end="")
                if (op[4] == "S2"):
                  if (op[3] == "AND"):
                    for i in range(n):
                      if (s3[i] == "0" and s2[i] == "0"):
                        s4.append("0")
                      if (s3[i] == "0" and s2[i] == "1"):
                        s4.append("0")
                      if (s3[i] == "1" and s2[i] == "0"):
                        s4.append("0")
                      if (s3[i] == "1" and s2[i] == "1"):
                        s4.append("1")
                    for i in range(n):
                      print(s4[i], end="")
                  if (op[3] == "OR"):
                    for i in range(n):
                      if (s3[i] == "0" and s2[i] == "0"):
                        s4.append("0")
                      if (s3[i] == "0" and s2[i] == "1"):
                        s4.append("1")
                      if (s3[i] == "1" and s2[i] == "0"):
                        s4.append("1")
                      if (s3[i] == "1" and s2[i] == "1"):
                        s4.append("1")
                    for i in range(n):
                      print(s4[i], end="")
                  if (op[3] == "XOR"):
                    for i in range(n):
                      if (s3[i] == "0" and s2[i] == "0"):
                        s4.append("0")
                      if (s3[i] == "0" and s2[i] == "1"):
                        s4.append("1")
                      if (s3[i] == "1" and s2[i] == "0"):
                        s4.append("1")
                      if (s3[i] == "1" and s2[i] == "1"):
                        s4.append("0")
                    for i in range(n):
                      print(s4[i], end="")
                  if (op[3] == "NAND"):
                    for i in range(n):
                      if (s3[i] == "0" and s2[i] == "0"):
                        s4.append("1")
                      if (s3[i] == "0" and s2[i] == "1"):
                        s4.append("1")
                      if (s3[i] == "1" and s2[i] == "0"):
                        s4.append("1")
                      if (s3[i] == "1" and s2[i] == "1"):
                        s4.append("0")
                    for i in range(n):
                      print(s4[i], end="")
                  if (op[3] == "NOR"):
                    for i in range(n):
                      if (s3[i] == "0" and s2[i] == "0"):
                        s4.append("1")
                      if (s3[i] == "0" and s2[i] == "1"):
                        s4.append("0")
                      if (s3[i] == "1" and s2[i] == "0"):
                        s4.append("0")
                      if (s3[i] == "1" and s2[i] == "1"):
                        s4.append("0")
                    for i in range(n):
                      print(s4[i], end="")
                  if (op[3] == "MOR"):
                    for i in range(n):
                      if (s3[i] == "0" and s2[i] == "0"):
                        s4.append("1")
                      if (s3[i] == "0" and s2[i] == "1"):
                        s4.append("1")
                      if (s3[i] == "1" and s2[i] == "0"):
                        s4.append("0")
                      if (s3[i] == "1" and s2[i] == "1"):
                        s4.append("1")
                    for i in range(n):
                      print(s4[i], end="")