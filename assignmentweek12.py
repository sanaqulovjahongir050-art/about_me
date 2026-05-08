def run_concrete_calculator():
    history=[]
    while True:
        length_str=input("Enter slab length in m (or 'q' to quit): ")
        if length_str.lower()=="q":
            break
        width_str="?"
        depth_str="?"
    
        try:
            length=float(length_str)
            if length<=0:
                raise ValueError("Length must be greater than zero")
            width_str=input("Enter sklab width in m: " )
            width= float(width_str)
            if width<=0:
                raise ValueError("Width must be greater than zero")
            depth_str = input("Enter slab depth in m : ")
            depth=float(depth_str)
            if depth<=0:
                raise ValueError("Depth must be greater than zero")
            volume=length*width*depth
            mass=volume*2400
        except ValueError as r:
                print(f"error:{r}")
                descriiption_str=f"{length_str}m*{depth_str}m * {width}m"

                history.append(descriiption_str,"Failure")
        else:
            print(f"Volume {volume:.3f}")
            print(f"MAss{mass:.1} ")
            descriiption_str=f"{length} m * {width} m * {depth}m"
        finally:
            print("----------")
        return history
    
