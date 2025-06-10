from openpyxl import load_workbook 

class Excel:
    def __init__(self):
        self.file_path = r"C:\Users\stars\OneDrive\Desktop\shopify_scrapping\products.xlsx"
        self.workbook = load_workbook(filename=self.file_path)
        
    #find the first cell that not filled with value
    def find_last_row(self, sheetname):
        for row in self.workbook[sheetname].iter_rows(max_col=1):
            for cell in row:
                if cell.value is not None:
                    last_cell = cell.coordinate
                    col = last_cell[:1]
                    row = int(last_cell[1:]) + 1
                    
                    
        return(col + str(row))
    
    

if __name__ == "__main__":
    excel = Excel()
    print(excel.find_last_row("Dog"))
