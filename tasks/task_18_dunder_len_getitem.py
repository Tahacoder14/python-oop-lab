"""
Task 18: Special Methods __len__ & __getitem__ - Making Objects Behave Like Collections
Concept:
Implement `__len__(self)` for `len(obj)` and `__getitem__(self, key)` for
indexing (`obj[key]`), slicing (`obj[start:stop]`), and iteration.
Let's create a 'WordCollection' that stores unique words.
"""

class WordCollection:
    def __init__(self, initial_words_str=""):
        # Store words in a set to ensure uniqueness, but convert to list for ordered access
        # This is a bit of a simplification for demo; a truly ordered set might be better.
        raw_words = [word.strip().lower() for word in initial_words_str.split(',') if word.strip()]
        self._words = sorted(list(set(raw_words))) # Unique, sorted words
        print(f"WordCollection created with words: {self._words}")

    def add_word(self, new_word):
        new_word_clean = new_word.strip().lower()
        if new_word_clean and new_word_clean not in self._words:
            self._words.append(new_word_clean)
            self._words.sort() # Keep it sorted
            print(f"Added '{new_word_clean}'. Collection: {self._words}")
        elif not new_word_clean:
            print("Cannot add empty word.")
        else:
            print(f"Word '{new_word_clean}' already in collection.")

    def __len__(self):
        print("WordCollection.__len__ called.")
        return len(self._words)

    def __getitem__(self, key):
        print(f"WordCollection.__getitem__ called with key: {key} (type: {type(key)})")
        if isinstance(key, int):
            # Basic positive/negative indexing
            return self._words[key]
        elif isinstance(key, slice):
            # Return a new WordCollection instance for slices to maintain type
            # For simplicity, just returning the sliced list:
            sliced_list = self._words[key]
            print(f"  Sliced to: {sliced_list}")
            return sliced_list # Or WordCollection(','.join(sliced_list))
        else:
            raise TypeError(f"WordCollection indices must be integers or slices, not {type(key).__name__}")

    def __str__(self):
        return f"WordCollection({len(self._words)} words: {', '.join(self._words)})"

    def __repr__(self):
        return f"WordCollection(initial_words_str='{','.join(self._words)}')"


def get_input_params():
    return [
        {"name": "initial_str", "label": "Initial Words (comma-separated):", "type": "text_input", "default": "apple,banana,apple,cherry,date,banana"},
        {"name": "word_to_add", "label": "Word to Add:", "type": "text_input", "default": "fig"},
        {"name": "index_to_get", "label": "Index to Retrieve (e.g., 0, -1):", "type": "number_input", "default": 0, "step":1, "format":"%d"},
        {"name": "slice_to_get", "label": "Slice (e.g., 1:3 for start:stop):", "type": "text_input", "default": "1:3"}
    ]

def run_task(initial_str, word_to_add, index_to_get, slice_to_get):
    my_collection = WordCollection(initial_str)
    print(str(my_collection))

    print(f"\n--- Adding '{word_to_add}' ---")
    my_collection.add_word(word_to_add)

    print("\n--- Using len() ---")
    print(f"Length of collection: {len(my_collection)}")

    print(f"\n--- Accessing by index {index_to_get} ---")
    try:
        item_at_index = my_collection[index_to_get]
        print(f"Word at index {index_to_get}: '{item_at_index}'")
    except IndexError as e:
        print(f"Error accessing index {index_to_get}: {e}")
    except TypeError as e: # If index_to_get isn't int
        print(f"Error: Index must be an integer. {e}")


    print(f"\n--- Accessing by slice '{slice_to_get}' ---")
    try:
        start_str, stop_str = slice_to_get.split(':')
        start = int(start_str) if start_str else None
        stop = int(stop_str) if stop_str else None
        custom_slice = slice(start, stop)
        sliced_items = my_collection[custom_slice]
        print(f"Words in slice my_collection[{slice_to_get}]: {sliced_items}")
    except ValueError:
        print(f"Invalid slice format '{slice_to_get}'. Use start:stop (e.g., 1:3 or :2 or 1:).")
    except IndexError as e:
        print(f"Error with slice {slice_to_get}: {e}")


    print("\n--- Iterating over the collection (uses __getitem__ implicitly) ---")
    print("Words in collection:")
    for word in my_collection: # This works due to __getitem__
        print(f"- {word}")

    print(f"\nIs 'cherry' in collection? {'cherry' in my_collection}") # Works due to iteration

if __name__ == "__main__":
    run_task("one,two,three,one", "four", 1, "0:2")