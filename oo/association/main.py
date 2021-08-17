'''
Uma classe está associada com a outra (uma usa a outra), porém, nenhuma das classes depende da outra.
Ou seja, elas não dependem entre si para existir.
'''

from classes import Writer, Pen, TypeWriter

writer = Writer('Machado de Assis')
pen = Pen('Bic')
machine = TypeWriter()

print(writer.name)
print(pen.brand)

# associação feita entre escritor e maquina de escrever (é o tipo de associação mais fraca)
writer.tool = machine
writer.tool.to_write()

del writer
# a caneta e a máquina continua existindo
print(pen.brand)
machine.to_write()