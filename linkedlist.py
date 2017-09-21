class LinkedList:
    """
    You should implement the methods of this class which are currently
    raising a NotImplementedError!
    Don't change the name of the class or any of the methods.
    """
    def __init__(self):
        self.__root = None

    def get_root(self):
        return self.__root

    def add_start_to_list(self, node):
        if self.__root:
            node.set_next(self.__root)
        self.__root = node
        

    def remove_end_from_list(self):
        marker = self.__root

        if not marker.get_next:
            self.__root = None
            return marker

        while marker:
            following_node = marker.get_next()
            if following_node:
                if not following_node.get_next():
                    marker.set_next(None)
                    return following_node
            marker = marker.get_next()


    def print_list(self):
        marker = self.__root
        while marker:
            marker.print_details()
            marker = marker.get_next()

    def find(self, name):
        marker = self.__root
        while marker:
            if marker.name == name:
                return marker
            marker = marker.get_next()
        raise LookupError("Name {} not founda in the linkedlist".format(name))

    def size(self):
        marker = self.__root
        count = 0
        while marker:
            count += 1
            marker = marker.get_next()
        return count

