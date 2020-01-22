from admin import Admin

eric = Admin('eric', 'jan', 'ericjan')
eric_privileges = [
        'can delete users',
        'can warn unfriendly comments',
        'can invite new users',
        ]
eric.privileges.privileges = eric_privileges
eric.privileges.show_privileges()
