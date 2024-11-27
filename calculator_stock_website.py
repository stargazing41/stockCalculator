import gradio as gr

def calculate_total_money_after_take_out(money, increase, length):
    money = int(money)
    increase = int(increase)
    length = int(length)
    cash = 0
    
    for i in range(length):
        cash += money
        cash = cash + (cash * (increase/100))

    cash = round(cash, 2)
    
    return cash

with gr.Blocks() as demo:
    gr.Markdown("# Stock Calculator")
    money = gr.Textbox(label="Money Text", placeholder = "How much money will you put in each year ex 100 (for 100 dollars): ")
    increase = gr.Textbox(label="Percent Increase", placeholder = "What percent will you gain each year ex 7 (for 7 percent): ")
    length = gr.Textbox(label="Time", placeholder = "How many years until you withdraw all your cash ex 10 (for 10 years): ")
    output = gr.Textbox(label="Money after given years")
    money_btn = gr.Button("Calculate")
    money_btn.click(fn=calculate_total_money_after_take_out, inputs = [money,increase,length], outputs = output)


demo.launch(share=True)