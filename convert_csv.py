import pandas as pd
import tkinter as tk
from tkinter import filedialog, messagebox

# Payment method master mapping
PAYMENT_MAPPING = {
    '代引き': 0,
    'クレジットカード': 1,
    '銀行振込': 2,
}

def convert_csv():
    """Open a CSV file, convert the payment method column and save."""
    file_path = filedialog.askopenfilename(
        title='Open CSV', filetypes=[('CSV files', '*.csv')]
    )
    if not file_path:
        return

    df = pd.read_csv(file_path)

    # Replace values in column E (5th column)
    if df.shape[1] >= 5:
        df.iloc[:, 4] = df.iloc[:, 4].map(PAYMENT_MAPPING).fillna(df.iloc[:, 4])

    save_path = filedialog.asksaveasfilename(
        title='Save CSV', defaultextension='.csv',
        filetypes=[('CSV files', '*.csv')]
    )
    if not save_path:
        return

    df.to_csv(save_path, index=False)
    messagebox.showinfo('Complete', 'Conversion completed and file saved.')


def main():
    root = tk.Tk()
    root.title('CSV Payment Converter')
    root.geometry('300x100')

    btn = tk.Button(root, text='Convert CSV', command=convert_csv)
    btn.pack(expand=True, pady=20)

    root.mainloop()

if __name__ == '__main__':
    main()
