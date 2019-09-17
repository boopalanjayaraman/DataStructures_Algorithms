
class Group(object):
    def __init__(self, _name):
        self.name = _name
        self.groups = []
        self.users = set() #changed this from array to a set
        #python set is backed by dict type and hence it is essentially like a hashset with O(1) performance for look-ups.
        #since only ids are going to be stored in users, it can be assumed to not contain any duplicates.
        #hence, set is more likely to be suitable 

    def add_group(self, group):
        self.groups.append(group)

    def add_user(self, user):
        self.users.add(user)

    def get_groups(self):
        return self.groups

    def get_users(self):
        return self.users

    def get_name(self):
        return self.name


def is_user_in_group(user, group):
    """
    Return True if user is in the group, False otherwise.

    Args:
      user(str): user name/id
      group(class:Group): group to check user membership against
    """
    if user in group.get_users():
        return True
    else:
        for child_group in group.get_groups():
            is_user_in_child_group = is_user_in_group(user, child_group)
            if is_user_in_child_group:
                return True
    return False

if __name__ == "__main__":
    parent = Group("parent")
    child = Group("child")
    sub_child = Group("subchild")

    sub_child_user = "sub_child_user"
    sub_child.add_user(sub_child_user)

    child.add_group(sub_child)
    parent.add_group(child)

    print(is_user_in_group(sub_child_user, sub_child)) #prints True
    print(is_user_in_group(sub_child_user, child)) #prints True
    print(is_user_in_group(sub_child_user, parent)) #prints True

    sub_child_user1 = "sub_child_user1"
    sub_child.add_user(sub_child_user1)

    child_user = "child_user"
    child.add_user(child_user)

    parent_user = "parent_user"
    parent.add_user(parent_user)

    print(is_user_in_group(child_user, sub_child)) #prints False
    print(is_user_in_group(parent_user, child)) #prints False
    print(is_user_in_group('', child)) #prints False
