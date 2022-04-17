if __name__ == "__main__":
   try:
       __import__("jimi").karma()
   except Exception as e:
       exit(str(e))
