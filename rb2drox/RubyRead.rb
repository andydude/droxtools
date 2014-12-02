require 'cgi'
require 'ast'
require 'parser/current'

def node_type_to_csymbol(node_type)
  cd, name = nil, nil

  case node_type.to_s
  when "alias"
    cd, name = "rb1", "alias"
  when "and"
    cd, name = "logic1", "and"
  when "array"
    cd, name = "rb1", "array"
  when "begin"
    cd, name = "prog2", "begin"
  when "block"
    cd, name = "prog1", "block"
  when "break"
    cd, name = "prog2", "break"
  when "case"
    cd, name = "rb1", "case"
  when "class"
    cd, name = "rb1", "class"
  when "defined?"
    cd, name = "rb1", "is_defined"
  when "do"
    cd, name = "rb1", "do"
  when "dregx"
    cd, name = "rb1", "dynamic_regexp"
  when "dstr"
    cd, name = "rb1", "dynamic_string"
  when "ensure"
    cd, name = "rb1", "ensure"
  when "erange"
    cd, name = "interval1", "interval_co"
  when "false"
    cd, name = "logic1", "false"
  when "hash"
    cd, name = "rb1", "hash"
  when "if"
    cd, name = "prog2", "if_exp"
  when "irange"
    cd, name = "interval1", "interval_cc"
  when "kwbegin"
    cd, name = "rb1", "kwbegin"
  when "masgn"
    cd, name = "rb1", "multiple_assignment"
  when "mlhs"
    cd, name = "rb1", "multiple_assignment_vars"
  when "module"
    cd, name = "rb1", "module"
  when "next"
    cd, name = "prog2", "continue"
  when "nil"
    cd, name = "prog2", "null"
  when "or"
    cd, name = "logic1", "or"
  when "pair"
    cd, name = "rb1", "pair"
  when "regexp"
    cd, name = "rb1", "regexp"
  when "require"
    cd, name = "rb1", "require"
  when "resbody"
    cd, name = "rb1", "resbody"
  when "rescue"
    cd, name = "rb1", "rescue"
  when "redo"
    cd, name = "rb1", "redo"
  when "retry"
    cd, name = "rb1", "retry"
  when "return"
    cd, name = "prog1", "return"
  when "sclass"
    cd, name = "rb1", "sclass"
  when "splat"
    cd, name = "rb1", "splat"
  when "self"
    cd, name = "rb1", "self"
  when "super"
    cd, name = "rb1", "super"
  when "true"
    cd, name = "logic1", "true"
  when "undef"
    cd, name = "rb1", "undef"
  when "unless"
    cd, name = "prog2", "if_not"
  when "until"
    cd, name = "prog2", "while_not"
  when "when"
    cd, name = "rb1", "when"
  when "while"
    cd, name = "prog1", "while"
  when "yield"
    cd, name = "rb1", "yield"
  else
    cd, name = "UNKNOWN", node_type
  end
  
  "<m:csymbol cd=\"#{cd}\">#{name}</m:csymbol>"
end

def method_name_to_csymbol(method_name)
  cd, name = nil, nil

  case method_name.to_s
  when ">>"
    cd, name = "bitwise1", "shift_right"
  when "<<"
    cd, name = "bitwise1", "shift_left"
  when ">="
    cd, name = "relation1", "geq"
  when ">"
    cd, name = "relation1", "gt"
  when "<="
    cd, name = "relation1", "leq"
  when "<"
    cd, name = "relation1", "lt"
  when "!="
    cd, name = "relation1", "neq"
  when "=="
    cd, name = "relation1", "eq"
  when "+"
    cd, name = "arith4", "plus"
  when "-"
    cd, name = "arith4", "minus"
  when "*"
    cd, name = "arith4", "times"
  when "&"
    cd, name = "rb1", "code_block_ref"
  when "^"
    cd, name = "arith4", "power"
  when "||"
    cd, name = "logic1", "or"
  when "&&"
    cd, name = "logic1", "and"
  when "new"
    cd, name = "prog2", "new"
  else
    return nil
  end
  
  "<m:csymbol cd=\"#{cd}\">#{name}</m:csymbol>"
end
  
def encode_string(s)
  return s.codepoints.to_a.map {|cp|
    if [0x09].include? cp
      [cp].pack("U*")
    elsif 0x00 <= cp and cp <= 0x1F
      "<m:cn type=\"character\">" + cp.to_s(10) + "</m:cn>"
    elsif 0x80 <= cp and cp <= 0x9F
      "<m:cn type=\"character\">" + cp.to_s(10) + "</m:cn>"
    else
      CGI.escapeHTML([cp].pack("U*"))
    end
  }.join("").encode("utf-8")
end

class DroseraProcessor < AST::Processor
  #def process_binary_op(node)
  #  left_expr, right_expr = *node
  #  puts "<m:apply>"
  #  process(left_expr)
  #  process(right_expr)
  #  puts "</m:apply>\n"
  #
  #  # AST::Node#updated won't change node type if nil is passed as a first
  #  # argument, which allows to reuse the same handler for multiple node types
  #  # using `alias' (below).
  #  node.updated(nil, [
  #                 process(left_expr),
  #                 process(right_expr)
  #               ])
  #end
  #alias on_add      process_binary_op
  #alias on_multiply process_binary_op
  #alias on_divide   process_binary_op
  #
  #def on_negate(node)
  #  # It is also possible to use #process_all for more compact code
  #  # if every child is a Node.
  #  node.updated(nil, process_all(node))
  #end
  #
  #def on_store(node)
  #  expr, variable_name = *node
  #
  #  # Note that variable_name is not a Node and thus isn't passed to #process.
  #  node.updated(nil, [
  #                 process(expr),
  #                 variable_name
  #               ])
  #end
  #
  ## (load) is effectively a terminal node, and so it does not need
  ## an explicit handler, as the following is the default behavior.
  #def on_load(node)
  #  nil
  #end
  #
  #def on_each(node)
  #  node.updated(nil, process_all(node))
  #end



  def process_constant_node(node)
    csym = node_type_to_csymbol(node.type)
    puts csym
    node
  end
  
  alias on_false    process_constant_node
  alias on_true     process_constant_node
  alias on_nil      process_constant_node
  
  def process_regular_node(node)
    csym = node_type_to_csymbol(node.type)
    puts "<m:apply>"
    puts csym
    process_all(node)
    puts "</m:apply>"
    node
  end

  alias on_dstr     process_regular_node
  alias on_dsym     process_regular_node
  alias on_regexp   process_regular_node
  alias on_xstr     process_regular_node
  alias on_splat    process_regular_node
  alias on_array    process_regular_node
  alias on_pair     process_regular_node
  alias on_hash     process_regular_node
  alias on_irange   process_regular_node
  alias on_erange   process_regular_node

  def on_var(node)
    name, *rest = *node
    puts "<m:ci class=\"#{node.type.to_s}\">#{encode_string(name.to_s)}</m:ci>"
    node
  end

  def process_variable_node(node)
    on_var(node)
  end

  alias on_lvar     process_variable_node
  alias on_ivar     process_variable_node
  alias on_gvar     process_variable_node
  alias on_cvar     process_variable_node
  alias on_back_ref process_variable_node
  alias on_nth_ref  process_variable_node

  def on_vasgn(node)
    name, value_node = *node
    
    puts "<drox:dl>"
    puts "<m:csymbol cd=\"prog1\">local_var vasgn</m:csymbol>"
    puts "<m:ci>#{name}</m:ci>"
    process(value_node)
    puts "</drox:dl>"

    node
  end

  def process_var_asgn_node(node)
    on_vasgn(node)
  end

  alias on_lvasgn   process_var_asgn_node
  alias on_ivasgn   process_var_asgn_node
  alias on_gvasgn   process_var_asgn_node
  alias on_cvasgn   process_var_asgn_node

  def on_op_asgn(node)
    var_node, method_name, value_node = *node
    
    puts "<m:apply>"
    puts "<m:csymbol cd=\"prog2\">assignment_operator_exp</m:csymbol>"
    puts method_name_to_csymbol(method_name)
    process(var_node)
    process(value_node)
    puts "</m:apply>"

    node
  end
  
  def on_and_asgn(node)
    var_node, value_node = *node
    
    puts "<m:apply>"
    puts "<m:csymbol cd=\"prog2\">assignment_operator_exp</m:csymbol>"
    puts "<m:csymbol cd=\"logic1\">and</m:csymbol>"
    process(var_node)
    process(value_node)
    puts "</m:apply>"

    node
  end
  
  def on_or_asgn(node)
    var_node, value_node = *node
    
    puts "<m:apply>"
    puts "<m:csymbol cd=\"prog2\">assignment_operator_exp</m:csymbol>"
    puts "<m:csymbol cd=\"logic1\">or</m:csymbol>"
    process(var_node)
    process(value_node)
    puts "</m:apply>"

    node
  end

  alias on_mlhs     process_regular_node
  alias on_masgn    process_regular_node

  def on_const(node)
    scope_node, name = *node
    
    if scope_node
      process(scope_node)
      puts "<m:ci type=\"rb:const\">#{scope_node}<m:sep/>#{name}</m:ci>"
    else
      puts "<m:ci type=\"rb:const\">#{name}</m:ci>"
    end
    
    node
  end

  def on_casgn(node)
    scope_node, name, value_node = *node

    if scope_node
      process(scope_node)
      puts "<m:ci type=\"rb:casgn\">#{scope_node}<m:sep/>#{name}</m:ci>"
    else
      puts "<m:ci type=\"rb:casgn\">#{name}</m:ci>"
      
    end
    process(value_node)
    
    node
  end

  def on_args(node)
    process_all(node)
    node
  end

  def on_argument(node)
    arg_name, value_node = *node

    puts "<m:bvar role=\"#{node.type}\">"
    puts "<m:ci>#{arg_name}</m:ci>"
    process(value_node)
    puts "</m:bvar>"

    node
  end

  def process_argument_node(node)
    on_argument(node)
  end

  alias on_arg            process_argument_node
  alias on_optarg         process_argument_node
  alias on_restarg        process_argument_node
  alias on_blockarg       process_argument_node
  alias on_shadowarg      process_argument_node
  alias on_kwarg          process_argument_node
  alias on_kwoptarg       process_argument_node
  alias on_kwrestarg      process_argument_node

  alias on_arg_expr       process_regular_node
  alias on_restarg_expr   process_regular_node
  alias on_blockarg_expr  process_regular_node

  alias on_module         process_regular_node
  alias on_class          process_regular_node
  alias on_sclass         process_regular_node

  def on_def(node)
    name, args_node, body_node = *node

    puts "<drox:dl>"
    puts "<m:csymbol cd=\"rb\">#{node.type}</m:csymbol>"
    puts "<drox:dt>"
    puts "<m:ci>#{name}</m:ci>"
    puts "</drox:dt>"
    process(args_node)
    process(body_node)
    puts "</drox:dl>\n"

    node
  end

  def on_defs(node)
    definee_node, name, args_node, body_node = *node

    puts "<drox:dl>"
    puts "<m:csymbol cd=\"rb\">#{node.type}</m:csymbol>"
    process(definee_node)
    puts "<drox:dt>"
    puts "<drox:#{definee_node.type}/>"
    puts "<m:ci>#{name}</m:ci>"
    puts "</drox:dt>"
    process(args_node)
    process(body_node)
    puts "</drox:dl>\n"

    node
  end

  alias on_undef    process_regular_node
  alias on_alias    process_regular_node

  def on_str(node)
    value, *rest = *node
    value = encode_string(value)
    puts "<m:cs xml:space=\"preserve\">#{value}</m:cs>"
    #value.encode(:xml => :text)
    #if value.ascii_only?
    #  value = value.encode('utf-8')
    #else
    #  puts "<m:cs>...</m:cs>"
    #end
    node
  end
  
  def on_int(node)
    value, *rest = *node
    puts "<m:cn type=\"integer\">#{value}</m:cn>"
    node
  end
  
  def on_send(node)
    receiver_node, method_name, *arg_nodes = *node
    
    puts "<m:apply>"
    if receiver_node then
      s = method_name_to_csymbol(method_name)
      if s
        puts s
      else
        puts "<m:ci>#{receiver_node.type}<m:sep/>#{method_name}</m:ci>"
      end
      process(receiver_node)
    else
      
      if method_name.to_s == "puts"
        puts "<m:csymbol cd=\"prog2\">println</m:csymbol>"
      elsif method_name.to_s == "print"
        puts "<m:csymbol cd=\"prog2\">print</m:csymbol>"
      else
        puts "<m:ci class='method'>#{method_name}</m:ci>"
      end
    end
    process_all(arg_nodes)
    puts "</m:apply>\n"

    node
  end

  alias on_block    process_regular_node

  alias on_while      process_regular_node
  alias on_while_post process_regular_node
  alias on_until      process_regular_node
  alias on_until_post process_regular_node
  alias on_for        process_regular_node

  alias on_return   process_regular_node
  alias on_break    process_regular_node
  alias on_next     process_regular_node
  alias on_redo     process_regular_node
  alias on_retry    process_regular_node
  alias on_super    process_regular_node
  alias on_yield    process_regular_node
  alias on_defined? process_regular_node

  alias on_not      process_regular_node
  alias on_and      process_regular_node
  alias on_or       process_regular_node

  alias on_if       process_regular_node

  alias on_when     process_regular_node
  alias on_case     process_regular_node

  alias on_iflipflop process_regular_node
  alias on_eflipflop process_regular_node

  alias on_match_current_line process_regular_node
  alias on_match_with_lvasgn  process_regular_node

  alias on_resbody  process_regular_node
  alias on_rescue   process_regular_node
  alias on_ensure   process_regular_node

  alias on_begin    process_regular_node
  alias on_kwbegin  process_regular_node

  alias on_preexe   process_regular_node
  alias on_postexe  process_regular_node
end

puts File.new("share/prolog.xmlf", "r").read()
source = IO.read(ARGV.shift)
ast, comments = Parser::CurrentRuby.parse_with_comments(source)
DroseraProcessor.new.process(ast)
puts File.new("share/epilog.xmlf", "r").read()
