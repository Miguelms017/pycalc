from pyscript import document, when

display_list = []

calc_array = []

@when ("click", ".button" )
def handle_click(event):
    display_list.append (event.target.innerText)
    document.querySelector("#show").innerText = "".join(display_list)

@when ("click", ".button-right" )
def handle_click(event): 
    operators = ["+", "-", "/", "*"]

    if len(calc_array) > 0 and calc_array in operators: 
        pass
    else:
        number = document.querySelector("#show").innerText
        calc_array.append (number)
        if event.target.innerText == 'X':
            calc_array.append ('*')
            print(calc_array)
            display_list.clear()
        elif event.target.innerText == "=":
            calc_array.append ('')
        else:
            calc_array.append (event.target.innerText)
            print(calc_array)
            display_list.clear()

@when ("click", "#delete")
def handle_click(event):
    if len(display_list) == 0:
        document.querySelector("#show").innerText = ""
    else:
        del display_list[-1]
        document.querySelector("#show").innerText = "".join(display_list)

@when ("click", "#clear")
def handle_click(event):
    display_list.clear()
    calc_array.clear()
    document.querySelector("#show").innerText = "".join(display_list)\


@when ("click", "#equal")
def handle_click(event):
    operators = ["+", "-", "/", "*"]

    if len(calc_array) == 0:
        pass
    elif calc_array[-1] in operators:
        pass
    else:
        exp = "".join(calc_array)

        try:
            total = eval(exp)
            document.querySelector("#show").innerText = total
            calc_array.clear()
            display_list.clear()

        except ZeroDivisionError:
            document.querySelector("#show").innerText = "Error, Please click AC"
            calc_array.clear()
            display_list.clear()