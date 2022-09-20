"""
Architecture-dependent configurations
"""

class ROPArch:
    def __init__(self, project):
        self.project = project
        self.max_sym_mem_access = 4
        self.alignment = project.arch.instruction_alignment
        # REVIEW: self.alignment*8 no sense....
        # it should considerate jump process progarm flow

        # HACK: What the fuck with max_block_size, it's really stupid to use that 
        # to certain the length of ropgadget
        # Reference: RopGadgets or ropper or rp++
        self.max_block_size = self.alignment * 8
        self.reg_list = self._get_reg_list()

        a = project.arch
        self.base_pointer = a.register_names[a.bp_offset]

        # self.disengine = project.arch.capstone

    def _get_reg_list(self):
        """
        get the list of names of general-purpose registers
        """
        arch = self.project.arch
        _sp_reg = arch.register_names[arch.sp_offset]
        _ip_reg = arch.register_names[arch.ip_offset]

        # get list of general-purpose registers
        self._reg_list = arch.default_symbolic_registers
        # prune the register list of the instruction pointer and the stack pointer
        return [r for r in self._reg_list if r not in (_sp_reg, _ip_reg)]

    def block_make_sense(self, block):
        return True

class X86(ROPArch):
    def __init__(self, project):
        super().__init__(project)
        self.max_block_size = 20 # X86 and AMD64 have alignment of 1, 8 bytes is certainly not good enough

    def block_make_sense(self, block):
        """
        TODO: check the block is a;; oh no need
        """
        capstr = str(block.capstone).lower()
        if 'cli' in capstr or 'rex' in capstr or "fs:" in capstr or "gs:" in capstr:
            return False
        if block.size < 1 or block.bytes[0] == 0x4f:
            return False
        return True

class AMD64(X86):
    pass

class PPC(ROPArch):
    pass

arm_conditional_postfix = ['eq', 'ne', 'cs', 'hs', 'cc', 'lo', 'mi', 'pl',
                           'vs', 'vc', 'hi', 'ls', 'ge', 'lt', 'gt', 'le', 'al']
class ARM(ROPArch):

    def __init__(self, project):
        super().__init__(project)
        self.is_thumb = False # by default, we don't use thumb mode

    def block_make_sense(self, block):
        # disable conditional jumps, for now
        # FIXME: we should handle conditional jumps, they are useful
        # print(block)
        for insn in block.capstone.insns:
            if insn.insn.mnemonic[-2:] in arm_conditional_postfix:
                return False
        return True

    """
    TODO: Reference Ropgadgets need more type of gadgets
    """
        
class MIPS(ROPArch):
    """
    Add MIPS support
    """
    pass

def get_arch(project):
    name = project.arch.name
    print(name)
    if name == 'X86':
        return X86(project)
    elif name == 'AMD64':
        return AMD64(project)
    elif name.startswith('ARM'):
        return ARM(project)
    elif name.startswith('MIPS'):
        return MIPS(project)
    else:
        raise ValueError(f"Unknown arch: {name}")
