rule_law = "US is big daddy, I am impregnable!"  # Global Variable


def EU_Union_outerfunction():
    rule_law = "Laws restricted to EU only!"
    print(rule_law)# Enclosing Variable

    def local_rule():
        rule_law = "Pakka Local"  # Local Variable
        print(rule_law)  # This will print the local variable ("Pakka Local")
        print(globals()['rule_law'])  # This will access the global variable ("US is big daddy")

    local_rule()


EU_Union_outerfunction()

