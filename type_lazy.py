
class TypeCheck:
    """
    All methods take two arguments: default_value, check_value
    If type(check_value) != the method's name type 
    EX: is_str is checking for type str()
    it will return default_value. Which can be any type.
    """
    @staticmethod
    def is_this(default_value:any = None, check_value:any = None, this_value:any = None):
        """
        If you want to compare unique types, please use this method.
        default_value:
        returned if type(check_value) != type(this_value)
        check_value:
        returned if type(check_value) == type(this_value)
        this_value:
        return default_value If type(check_value) != type(this_value)
        Do not input the datatype for this_value
        The method will inspect the type.                    
        """
        return default_value if not isinstance(check_value, type(this_value)) else check_value
    
    @staticmethod
    def is_str(default_value:any = None, check_value:str = None):
        """return check_value if str() else return default_value"""
        return default_value if not isinstance(check_value, str) else check_value

    @staticmethod
    def is_int(default_value:any = None, check_value:int = None):
        """return check_value if int() else return default_value"""
        return default_value if not isinstance(check_value, int) else check_value

    @staticmethod
    def is_set(default_value:any = None, check_value:set = None):
        """return check_value if set() else return default_value"""
        return default_value if not isinstance(check_value, set) else check_value

    @staticmethod
    def is_list(default_value:any = None, check_value:list = None):
        """return check_value if list() else return default_value"""
        return default_value if not isinstance(check_value, list) else check_value

    @staticmethod
    def is_dict(default_value:any = None, check_value:dict = None):
        """return check_value if dict() else return default_value"""
        return default_value if not isinstance(check_value, dict) else check_value

    @staticmethod
    def is_float(default_value:any = None, check_value:float = None):
        """return check_value if float() else return default_value"""
        return default_value if not isinstance(check_value, float) else check_value

    @staticmethod
    def is_bool(default_value:any = None, check_value:bool = None):
        """return check_value if bool() else return default_value"""
        return default_value if not isinstance(check_value, bool) else check_value
    
    @staticmethod
    def test_methods():
        """Terrible way of testing"""
        
        assert TypeCheck.is_this("test default value", "testing good input for is_this", "string_test")
        assert TypeCheck.is_this("testing bad input for is_str", 3, "int")
        assert TypeCheck.is_this("testing bad input for is_str", 3.14, "float")
        assert TypeCheck.is_this("testing bad input for is_str", ["this shouldn't work"], "list")
        
        assert TypeCheck.is_str("test default value", "testing good input for is_str")
        assert TypeCheck.is_str("testing bad input for is_str", 3)
        assert TypeCheck.is_str("testing bad input for is_str", 3.14)
        assert TypeCheck.is_str("testing bad input for is_str", ["this shouldn't work"])
        
        assert TypeCheck.is_int("test default value", 3)
        assert TypeCheck.is_int("testing bad input for is_int", "3")
        assert TypeCheck.is_int("testing bad input for is_int", 3.14)
        assert TypeCheck.is_int("testing bad input for is_int", ["this shouldn't work"])
        
        assert TypeCheck.is_set("test default value for is_set", {3})
        assert TypeCheck.is_set("testing bad input for is_set", 3)
        assert TypeCheck.is_set("testing bad input for is_set", 3.14)
        assert TypeCheck.is_set("testing bad input for is_set", ["this shouldn't work"])
        
        assert TypeCheck.is_list("test default value", ["this should work"])
        assert TypeCheck.is_list("testing bad input for is_list", 3)
        assert TypeCheck.is_list("testing bad input for is_list", 3.14)
        assert TypeCheck.is_list("testing bad input for is_list", "this shouldn't work")
        
        assert TypeCheck.is_dict("test default value", {"test_dict" : "this should work"})
        assert TypeCheck.is_dict("testing bad input for is_dict", 3)
        assert TypeCheck.is_dict("testing bad input for is_dict", 3.14)
        assert TypeCheck.is_dict("testing bad input for is_dict", ["this shouldn't work"])
        
        assert TypeCheck.is_float("test default value", 3.14)
        assert TypeCheck.is_float("testing bad input for is_float", 3)
        assert TypeCheck.is_float("testing bad input for is_float", "3.14")
        assert TypeCheck.is_float("testing bad input for is_float", ["this shouldn't work"])
