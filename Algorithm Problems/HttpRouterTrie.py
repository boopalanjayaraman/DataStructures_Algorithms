class RouteTrieNode:
    def __init__(self, handler = None):
        # Initialize the node with children as before, plus a handler
        self.children = {}
        self.handler = handler

    def insert(self, path_section):
        # Insert the node as before
        if path_section not in self.children:
            self.children[path_section] = RouteTrieNode()
        
        return self.children[path_section]

class RouteTrie:
    def __init__(self, root_handler):
        # Initialize the trie with an root node and a handler, this is the root path or home page node
        self.root = RouteTrieNode(root_handler)

    def insert(self, path_sections, handler):
        # Similar to our previous example you will want to recursively add nodes
        # Make sure you assign the handler to only the leaf (deepest) node of this path
        node = self.root
        for path_section in path_sections:
            node = node.insert(path_section)
        node.handler = handler

    def find(self, path_sections):
        # Starting at the root, navigate the Trie to find a match for this path
        # Return the handler for a match, or None for no match
        node = self.root
        for path_section in path_sections:
            if path_section not in node.children:
                return None
            node = node.children[path_section]

        return node.handler

# The Router class will wrap the Trie and handle 
class Router:
    def __init__(self, root_handler, not_found_handler):
        # Create a new RouteTrie for holding our routes
        # You could also add a handler for 404 page not found responses as well!
        self.router = RouteTrie(root_handler)
        self.not_found_handler = not_found_handler

    def add_handler(self, full_path, handler):
        # Add a handler for a path
        # You will need to split the path and pass the pass parts
        # as a list to the RouteTrie
        path_sections = self.split_path(full_path)
        self.router.insert(path_sections, handler)

    def lookup(self, full_path):
        # lookup path (by parts) and return the associated handler
        # you can return None if it's not found or
        # return the "not found" handler if you added one
        # bonus points if a path works with and without a trailing slash
        # e.g. /about and /about/ both return the /about handler
        path_sections = self.split_path(full_path)
        handler = self.router.find(path_sections)
        if handler is None:
            return self.not_found_handler
        else:
            return handler


    def split_path(self, full_path):
        # you need to split the path into parts for 
        # both the add_handler and loopup functions,
        # so it should be placed in a function here
        path_sections = [path_section for path_section in full_path.split('/') if path_section != '']
        return path_sections


if __name__ == "__main__":
    # Here are some test cases and expected outputs you can use to test your implementation

    # create the router and add a route
    router = Router("root handler", "not found handler") # remove the 'not found handler' if you did not implement this
    router.add_handler("/home/about", "about handler")  # add a route

    # some lookups with the expected output
    print(router.lookup("/")) # prints 'root handler'
    print(router.lookup("/home")) # prints 'not found handler' 
    print(router.lookup("/home/about")) # prints 'about handler'
    print(router.lookup("/home/about/")) # prints 'about handler' 
    print(router.lookup("/home/about/me")) # prints 'not found handler'

    router.add_handler("/home", "home handler")
    router.add_handler("/home/contact", "contact handler")
    router.add_handler("/home/login", "login handler")

    print(router.lookup("/home")) # prints 'home handler' 
    print(router.lookup("/home/contact")) # prints 'contact handler'
    print(router.lookup("/home/login/")) # prints 'login handler' 