# Single Responsibility Principle
class Journal:
    def __init__(self):
        self.entries = []
        self.count = 0

    def add_entry(self, text):
        self.entries.append(f"{self.count}: {text}")
        self.count += 1

    def remove_entry(self, pos):
        del self.entries[pos]

    def __str__(self):
        return "\n".join(self.entries)

    # break SRP !!!
    def save(self, filename):
        file = open(filename, "w")
        file.write(str(self))
        file.close()

    # break SRP !!!
    def load(self, filename):
        pass

    # break SRP !!!
    def load_from_web(self, uri):
        pass


class PersistenceManager:
    @staticmethod
    def save_to_file(journal, filename):
        file = open(filename, "w")
        file.write(str(journal))
        file.close()


j = Journal()
j.add_entry("I cried today.")
j.add_entry("I ate a bug.")
print(f"Journal entries:\n{j}\n")

p = PersistenceManager()
file = r'c:\temp\journal.txt'
p.save_to_file(j, file)

# verify!
with open(file) as fh:
    text = fh.read()
    print(text)
    assert text == str(j)
