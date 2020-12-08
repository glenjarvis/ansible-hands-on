#!/usr/bin/python
# -*- coding: utf-8 -*-

# (c) 2012, Michael DeHaan <michael.dehaan@gmail.com>, and others
#
# This file is part of Ansible
#
# Ansible is free software: you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.
#
# Ansible is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with Ansible.  If not, see <http://www.gnu.org/licenses/>.

import sys
import datetime
import traceback
import re
import shlex
import os

DOCUMENTATION = '''
---
module: command
version_added: historical
short_description: Executes a command on a remote node
description:
     - The M(command) module takes the command name followed by a list of space-delimited arguments.
     - The given command will be executed on all selected nodes. It will not be
       processed through the shell, so variables like C($HOME) and operations
       like C("<"), C(">"), C("|"), and C("&") will not work (use the M(shell)
       module if you need these features).
options:
  free_form:
    description:
      - the command module takes a free form command to run.  There is no parameter actually named 'free form'.
        See the examples!
    required: true
    default: null
    aliases: []
  creates:
    description:
      - a filename, when it already exists, this step will B(not) be run.
    required: no
    default: null
  removes:
    description:
      - a filename, when it does not exist, this step will B(not) be run.
    version_added: "0.8"
    required: no
    default: null
  chdir:
    description:
      - cd into this directory before running the command
    version_added: "0.6"
    required: false
    default: null
  executable:
    description:
      - change the shell used to execute the command. Should be an absolute path to the executable.
    required: false
    default: null
    version_added: "0.9"
notes:
    -  If you want to run a command through the shell (say you are using C(<),
       C(>), C(|), etc), you actually want the M(shell) module instead. The
       M(command) module is much more secure as it's not affected by the user's
       environment.
    -  " C(creates), C(removes), and C(chdir) can be specified after the command. For instance, if you only want to run a command if a certain file does not exist, use this."
author: Michael DeHaan
'''

EXAMPLES = '''
# Example from Ansible Playbooks
- command: /sbin/shutdown -t now

# Run the command if the specified file does not exist
- command: /usr/bin/make_database.sh arg1 arg2 creates=/path/to/database
'''

def main():

    # the command module is the one ansible module that does not take key=value args
    # hence don't copy this one if you are looking to build others!
    module = CommandModule(argument_spec=dict())

    shell = module.params['shell']
    chdir = module.params['chdir']
    executable = module.params['executable']
    args  = module.params['args']
    creates  = module.params['creates']
    removes  = module.params['removes']

    if args.strip() == '':
        module.fail_json(rc=256, msg="no command given")

    if chdir:
        os.chdir(chdir)

    if creates:
        # do not run the command if the line contains creates=filename
        # and the filename already exists.  This allows idempotence
        # of command executions.
        v = os.path.expanduser(creates)
        if os.path.exists(v):
            module.exit_json(
                cmd=args,
                stdout="skipped, since %s exists" % v,
                skipped=True,
                changed=False,
                stderr=False,
                rc=0
            )

    if removes:
    # do not run the command if the line contains removes=filename
    # and the filename does not exist.  This allows idempotence
    # of command executions.
        v = os.path.expanduser(removes)
        if not os.path.exists(v):
            module.exit_json(
                cmd=args,
                stdout="skipped, since %s does not exist" % v,
                skipped=True,
                changed=False,
                stderr=False,
                rc=0
            )

    if not shell:
        args = shlex.split(args)
    startd = datetime.datetime.now()

    rc, out, err = module.run_command(args, executable=executable, use_unsafe_shell=shell)

    endd = datetime.datetime.now()
    delta = endd - startd

    if out is None:
        out = ''
    if err is None:
        err = ''

    module.exit_json(
        cmd     = args,
        stdout  = out.rstrip("\r\n"),
        stderr  = err.rstrip("\r\n"),
        rc      = rc,
        start   = str(startd),
        end     = str(endd),
        delta   = str(delta),
        changed = True
    )

# import module snippets
# This code is part of Ansible, but is an independent component.
# This particular file snippet, and this file snippet only, is BSD licensed.
# Modules you write using this snippet, which is embedded dynamically by Ansible
# still belong to the author of the module, and may assign their own license
# to the complete work.
# 
# Copyright (c), Michael DeHaan <michael.dehaan@gmail.com>, 2012-2013
# All rights reserved.
#
# Redistribution and use in source and binary forms, with or without modification, 
# are permitted provided that the following conditions are met:
#
#    * Redistributions of source code must retain the above copyright 
#      notice, this list of conditions and the following disclaimer.
#    * Redistributions in binary form must reproduce the above copyright notice, 
#      this list of conditions and the following disclaimer in the documentation 
#      and/or other materials provided with the distribution.
#
# THIS SOFTWARE IS PROVIDED BY THE COPYRIGHT HOLDERS AND CONTRIBUTORS "AS IS" AND 
# ANY EXPRESS OR IMPLIED WARRANTIES, INCLUDING, BUT NOT LIMITED TO, THE IMPLIED 
# WARRANTIES OF MERCHANTABILITY AND FITNESS FOR A PARTICULAR PURPOSE ARE DISCLAIMED. 
# IN NO EVENT SHALL THE COPYRIGHT HOLDER OR CONTRIBUTORS BE LIABLE FOR ANY DIRECT, INDIRECT, 
# INCIDENTAL, SPECIAL, EXEMPLARY, OR CONSEQUENTIAL DAMAGES (INCLUDING, BUT NOT LIMITED TO, 
# PROCUREMENT OF SUBSTITUTE GOODS OR SERVICES; LOSS OF USE, DATA, OR PROFITS; OR BUSINESS 
# INTERRUPTION) HOWEVER CAUSED AND ON ANY THEORY OF LIABILITY, WHETHER IN CONTRACT, STRICT 
# LIABILITY, OR TORT (INCLUDING NEGLIGENCE OR OTHERWISE) ARISING IN ANY WAY OUT OF THE 
# USE OF THIS SOFTWARE, EVEN IF ADVISED OF THE POSSIBILITY OF SUCH DAMAGE.
#

# == BEGIN DYNAMICALLY INSERTED CODE ==

MODULE_ARGS = 'yum update'
MODULE_COMPLEX_ARGS = '{}'

BOOLEANS_TRUE = ['yes', 'on', '1', 'true', 1]
BOOLEANS_FALSE = ['no', 'off', '0', 'false', 0]
BOOLEANS = BOOLEANS_TRUE + BOOLEANS_FALSE

# ansible modules can be written in any language.  To simplify
# development of Python modules, the functions available here
# can be inserted in any module source automatically by including
# #<<INCLUDE_ANSIBLE_MODULE_COMMON>> on a blank line by itself inside
# of an ansible module. The source of this common code lives
# in lib/ansible/module_common.py

import os
import re
import pipes
import shlex
import subprocess
import sys
import syslog
import types
import time
import shutil
import stat
import tempfile
import traceback
import grp
import pwd
import platform
import errno
import tempfile

try:
    import json
except ImportError:
    try:
        import simplejson as json
    except ImportError:
        sys.stderr.write('Error: ansible requires a json module, none found!')
        sys.exit(1)
    except SyntaxError:
        sys.stderr.write('SyntaxError: probably due to json and python being for different versions')
        sys.exit(1)

HAVE_SELINUX=False
try:
    import selinux
    HAVE_SELINUX=True
except ImportError:
    pass

HAVE_HASHLIB=False
try:
    from hashlib import md5 as _md5
    HAVE_HASHLIB=True
except ImportError:
    from md5 import md5 as _md5

try:
    from hashlib import sha256 as _sha256
except ImportError:
    pass

try:
    from systemd import journal
    has_journal = True
except ImportError:
    import syslog
    has_journal = False

FILE_COMMON_ARGUMENTS=dict(
    src = dict(),
    mode = dict(),
    owner = dict(),
    group = dict(),
    seuser = dict(),
    serole = dict(),
    selevel = dict(),
    setype = dict(),
    # not taken by the file module, but other modules call file so it must ignore them.
    content = dict(),
    backup = dict(),
    force = dict(),
    remote_src = dict(), # used by assemble
    delimiter = dict(), # used by assemble
    directory_mode = dict(), # used by copy
)


def get_platform():
    ''' what's the platform?  example: Linux is a platform. '''
    return platform.system()

def get_distribution():
    ''' return the distribution name '''
    if platform.system() == 'Linux':
        try:
            distribution = platform.linux_distribution()[0].capitalize()
            if not distribution and os.path.isfile('/etc/system-release'):
                distribution = platform.linux_distribution(supported_dists=['system'])[0].capitalize()
                if 'Amazon' in distribution:
                    distribution = 'Amazon'
                else:
                    distribution = 'OtherLinux'
        except:
            # FIXME: MethodMissing, I assume?
            distribution = platform.dist()[0].capitalize()
    else:
        distribution = None
    return distribution

def load_platform_subclass(cls, *args, **kwargs):
    '''
    used by modules like User to have different implementations based on detected platform.  See User
    module for an example.
    '''

    this_platform = get_platform()
    distribution = get_distribution()
    subclass = None

    # get the most specific superclass for this platform
    if distribution is not None:
        for sc in cls.__subclasses__():
            if sc.distribution is not None and sc.distribution == distribution and sc.platform == this_platform:
                subclass = sc
    if subclass is None:
        for sc in cls.__subclasses__():
            if sc.platform == this_platform and sc.distribution is None:
                subclass = sc
    if subclass is None:
        subclass = cls

    return super(cls, subclass).__new__(subclass)


class AnsibleModule(object):

    def __init__(self, argument_spec, bypass_checks=False, no_log=False,
        check_invalid_arguments=True, mutually_exclusive=None, required_together=None,
        required_one_of=None, add_file_common_args=False, supports_check_mode=False):

        '''
        common code for quickly building an ansible module in Python
        (although you can write modules in anything that can return JSON)
        see library/* for examples
        '''

        self.argument_spec = argument_spec
        self.supports_check_mode = supports_check_mode
        self.check_mode = False
        self.no_log = no_log
        
        self.aliases = {}
        
        if add_file_common_args:
            for k, v in FILE_COMMON_ARGUMENTS.iteritems():
                if k not in self.argument_spec:
                    self.argument_spec[k] = v

        (self.params, self.args) = self._load_params()

        self._legal_inputs = ['CHECKMODE', 'NO_LOG']
        
        self.aliases = self._handle_aliases()

        if check_invalid_arguments:
            self._check_invalid_arguments()
        self._check_for_check_mode()
        self._check_for_no_log()

        # check exclusive early 
        if not bypass_checks:
            self._check_mutually_exclusive(mutually_exclusive)

        self._set_defaults(pre=True)

        if not bypass_checks:
            self._check_required_arguments()
            self._check_argument_values()
            self._check_argument_types()
            self._check_required_together(required_together)
            self._check_required_one_of(required_one_of)

        self._set_defaults(pre=False)
        if not self.no_log:
            self._log_invocation()

        # finally, make sure we're in a sane working dir
        self._set_cwd()

    def load_file_common_arguments(self, params):
        '''
        many modules deal with files, this encapsulates common
        options that the file module accepts such that it is directly
        available to all modules and they can share code.
        '''

        path = params.get('path', params.get('dest', None))
        if path is None:
            return {}
        else:
            path = os.path.expanduser(path)

        mode   = params.get('mode', None)
        owner  = params.get('owner', None)
        group  = params.get('group', None)

        # selinux related options
        seuser    = params.get('seuser', None)
        serole    = params.get('serole', None)
        setype    = params.get('setype', None)
        selevel   = params.get('selevel', None)
        secontext = [seuser, serole, setype]

        if self.selinux_mls_enabled():
            secontext.append(selevel)

        default_secontext = self.selinux_default_context(path)
        for i in range(len(default_secontext)):
            if i is not None and secontext[i] == '_default':
                secontext[i] = default_secontext[i]

        return dict(
            path=path, mode=mode, owner=owner, group=group,
            seuser=seuser, serole=serole, setype=setype,
            selevel=selevel, secontext=secontext,
        )


    # Detect whether using selinux that is MLS-aware.
    # While this means you can set the level/range with
    # selinux.lsetfilecon(), it may or may not mean that you
    # will get the selevel as part of the context returned
    # by selinux.lgetfilecon().

    def selinux_mls_enabled(self):
        if not HAVE_SELINUX:
            return False
        if selinux.is_selinux_mls_enabled() == 1:
            return True
        else:
            return False

    def selinux_enabled(self):
        if not HAVE_SELINUX:
            seenabled = self.get_bin_path('selinuxenabled')
            if seenabled is not None:
                (rc,out,err) = self.run_command(seenabled)
                if rc == 0:
                    self.fail_json(msg="Aborting, target uses selinux but python bindings (libselinux-python) aren't installed!")
            return False
        if selinux.is_selinux_enabled() == 1:
            return True
        else:
            return False

    # Determine whether we need a placeholder for selevel/mls
    def selinux_initial_context(self):
        context = [None, None, None]
        if self.selinux_mls_enabled():
            context.append(None)
        return context

    def _to_filesystem_str(self, path):
        '''Returns filesystem path as a str, if it wasn't already.

        Used in selinux interactions because it cannot accept unicode
        instances, and specifying complex args in a playbook leaves
        you with unicode instances.  This method currently assumes
        that your filesystem encoding is UTF-8.

        '''
        if isinstance(path, unicode):
            path = path.encode("utf-8")
        return path

    # If selinux fails to find a default, return an array of None
    def selinux_default_context(self, path, mode=0):
        context = self.selinux_initial_context()
        if not HAVE_SELINUX or not self.selinux_enabled():
            return context
        try:
            ret = selinux.matchpathcon(self._to_filesystem_str(path), mode)
        except OSError:
            return context
        if ret[0] == -1:
            return context
        # Limit split to 4 because the selevel, the last in the list,
        # may contain ':' characters
        context = ret[1].split(':', 3)
        return context

    def selinux_context(self, path):
        context = self.selinux_initial_context()
        if not HAVE_SELINUX or not self.selinux_enabled():
            return context
        try:
            ret = selinux.lgetfilecon_raw(self._to_filesystem_str(path))
        except OSError, e:
            if e.errno == errno.ENOENT:
                self.fail_json(path=path, msg='path %s does not exist' % path)
            else:
                self.fail_json(path=path, msg='failed to retrieve selinux context')
        if ret[0] == -1:
            return context
        # Limit split to 4 because the selevel, the last in the list,
        # may contain ':' characters
        context = ret[1].split(':', 3)
        return context

    def user_and_group(self, filename):
        filename = os.path.expanduser(filename)
        st = os.lstat(filename)
        uid = st.st_uid
        gid = st.st_gid
        return (uid, gid)

    def find_mount_point(self, path):
        path = os.path.abspath(os.path.expanduser(os.path.expandvars(path)))
        while not os.path.ismount(path):
            path = os.path.dirname(path)
        return path

    def is_nfs_path(self, path):
        """
        Returns a tuple containing (True, selinux_context) if the given path
        is on a NFS mount point, otherwise the return will be (False, None).
        """
        try:
            f = open('/proc/mounts', 'r')
            mount_data = f.readlines()
            f.close()
        except:
            return (False, None)
        path_mount_point = self.find_mount_point(path)
        for line in mount_data:
            (device, mount_point, fstype, options, rest) = line.split(' ', 4)
            if path_mount_point == mount_point and 'nfs' in fstype:
                nfs_context = self.selinux_context(path_mount_point)
                return (True, nfs_context)
        return (False, None)

    def set_default_selinux_context(self, path, changed):
        if not HAVE_SELINUX or not self.selinux_enabled():
            return changed
        context = self.selinux_default_context(path)
        return self.set_context_if_different(path, context, False)

    def set_context_if_different(self, path, context, changed):

        if not HAVE_SELINUX or not self.selinux_enabled():
            return changed
        cur_context = self.selinux_context(path)
        new_context = list(cur_context)
        # Iterate over the current context instead of the
        # argument context, which may have selevel.

        (is_nfs, nfs_context) = self.is_nfs_path(path)
        if is_nfs:
            new_context = nfs_context
        else:
            for i in range(len(cur_context)):
                if len(context) > i:
                    if context[i] is not None and context[i] != cur_context[i]:
                        new_context[i] = context[i]
                    if context[i] is None:
                        new_context[i] = cur_context[i]

        if cur_context != new_context:
            try:
                if self.check_mode:
                    return True
                rc = selinux.lsetfilecon(self._to_filesystem_str(path),
                                         str(':'.join(new_context)))
            except OSError:
                self.fail_json(path=path, msg='invalid selinux context', new_context=new_context, cur_context=cur_context, input_was=context)
            if rc != 0:
                self.fail_json(path=path, msg='set selinux context failed')
            changed = True
        return changed

    def set_owner_if_different(self, path, owner, changed):
        path = os.path.expanduser(path)
        if owner is None:
            return changed
        orig_uid, orig_gid = self.user_and_group(path)
        try:
            uid = int(owner)
        except ValueError:
            try:
                uid = pwd.getpwnam(owner).pw_uid
            except KeyError:
                self.fail_json(path=path, msg='chown failed: failed to look up user %s' % owner)
        if orig_uid != uid:
            if self.check_mode:
                return True
            try:
                os.lchown(path, uid, -1)
            except OSError:
                self.fail_json(path=path, msg='chown failed')
            changed = True
        return changed

    def set_group_if_different(self, path, group, changed):
        path = os.path.expanduser(path)
        if group is None:
            return changed
        orig_uid, orig_gid = self.user_and_group(path)
        try:
            gid = int(group)
        except ValueError:
            try:
                gid = grp.getgrnam(group).gr_gid
            except KeyError:
                self.fail_json(path=path, msg='chgrp failed: failed to look up group %s' % group)
        if orig_gid != gid:
            if self.check_mode:
                return True
            try:
                os.lchown(path, -1, gid)
            except OSError:
                self.fail_json(path=path, msg='chgrp failed')
            changed = True
        return changed

    def set_mode_if_different(self, path, mode, changed):
        path = os.path.expanduser(path)
        if mode is None:
            return changed
        try:
            # FIXME: support English modes
            if not isinstance(mode, int):
                mode = int(mode, 8)
        except Exception, e:
            self.fail_json(path=path, msg='mode needs to be something octalish', details=str(e))

        st = os.lstat(path)
        prev_mode = stat.S_IMODE(st[stat.ST_MODE])

        if prev_mode != mode:
            if self.check_mode:
                return True
            # FIXME: comparison against string above will cause this to be executed
            # every time
            try:
                if 'lchmod' in dir(os):
                    os.lchmod(path, mode)
                else:
                    os.chmod(path, mode)
            except OSError, e:
                if os.path.islink(path) and e.errno == errno.EPERM:  # Can't set mode on symbolic links
                    pass
                elif e.errno == errno.ENOENT: # Can't set mode on broken symbolic links
                    pass
                else:
                    raise e
            except Exception, e:
                self.fail_json(path=path, msg='chmod failed', details=str(e))

            st = os.lstat(path)
            new_mode = stat.S_IMODE(st[stat.ST_MODE])

            if new_mode != prev_mode:
                changed = True
        return changed

    def set_fs_attributes_if_different(self, file_args, changed):
        # set modes owners and context as needed
        changed = self.set_context_if_different(
            file_args['path'], file_args['secontext'], changed
        )
        changed = self.set_owner_if_different(
            file_args['path'], file_args['owner'], changed
        )
        changed = self.set_group_if_different(
            file_args['path'], file_args['group'], changed
        )
        changed = self.set_mode_if_different(
            file_args['path'], file_args['mode'], changed
        )
        return changed

    def set_directory_attributes_if_different(self, file_args, changed):
        return self.set_fs_attributes_if_different(file_args, changed)

    def set_file_attributes_if_different(self, file_args, changed):
        return self.set_fs_attributes_if_different(file_args, changed)

    def add_path_info(self, kwargs):
        '''
        for results that are files, supplement the info about the file
        in the return path with stats about the file path.
        '''

        path = kwargs.get('path', kwargs.get('dest', None))
        if path is None:
            return kwargs
        if os.path.exists(path):
            (uid, gid) = self.user_and_group(path)
            kwargs['uid'] = uid
            kwargs['gid'] = gid
            try:
                user = pwd.getpwuid(uid)[0]
            except KeyError:
                user = str(uid)
            try:
                group = grp.getgrgid(gid)[0]
            except KeyError:
                group = str(gid)
            kwargs['owner'] = user
            kwargs['group'] = group
            st = os.lstat(path)
            kwargs['mode']  = oct(stat.S_IMODE(st[stat.ST_MODE]))
            # secontext not yet supported
            if os.path.islink(path):
                kwargs['state'] = 'link'
            elif os.path.isdir(path):
                kwargs['state'] = 'directory'
            elif os.stat(path).st_nlink > 1:
                kwargs['state'] = 'hard'
            else:
                kwargs['state'] = 'file'
            if HAVE_SELINUX and self.selinux_enabled():
                kwargs['secontext'] = ':'.join(self.selinux_context(path))
            kwargs['size'] = st[stat.ST_SIZE]
        else:
            kwargs['state'] = 'absent'
        return kwargs


    def _handle_aliases(self):
        aliases_results = {} #alias:canon
        for (k,v) in self.argument_spec.iteritems():
            self._legal_inputs.append(k)
            aliases = v.get('aliases', None)
            default = v.get('default', None)
            required = v.get('required', False)
            if default is not None and required:
                # not alias specific but this is a good place to check this
                self.fail_json(msg="internal error: required and default are mutally exclusive for %s" % k)
            if aliases is None:
                continue
            if type(aliases) != list:
                self.fail_json(msg='internal error: aliases must be a list')
            for alias in aliases:
                self._legal_inputs.append(alias)
                aliases_results[alias] = k
                if alias in self.params:
                    self.params[k] = self.params[alias]
        
        return aliases_results

    def _check_for_check_mode(self):
        for (k,v) in self.params.iteritems():
            if k == 'CHECKMODE':
                if not self.supports_check_mode:
                    self.exit_json(skipped=True, msg="remote module does not support check mode")
                if self.supports_check_mode:
                    self.check_mode = True

    def _check_for_no_log(self):
        for (k,v) in self.params.iteritems():
            if k == 'NO_LOG':
                self.no_log = self.boolean(v)

    def _check_invalid_arguments(self):
        for (k,v) in self.params.iteritems():
            # these should be in legal inputs already
            #if k in ('CHECKMODE', 'NO_LOG'):
            #    continue
            if k not in self._legal_inputs:
                self.fail_json(msg="unsupported parameter for module: %s" % k)

    def _count_terms(self, check):
        count = 0
        for term in check:
            if term in self.params:
                count += 1
        return count

    def _check_mutually_exclusive(self, spec):
        if spec is None:
            return
        for check in spec:
            count = self._count_terms(check)
            if count > 1:
                self.fail_json(msg="parameters are mutually exclusive: %s" % check)

    def _check_required_one_of(self, spec):
        if spec is None:
            return
        for check in spec:
            count = self._count_terms(check)
            if count == 0:
                self.fail_json(msg="one of the following is required: %s" % ','.join(check))

    def _check_required_together(self, spec):
        if spec is None:
            return
        for check in spec:
            counts = [ self._count_terms([field]) for field in check ]
            non_zero = [ c for c in counts if c > 0 ]
            if len(non_zero) > 0:
                if 0 in counts:
                    self.fail_json(msg="parameters are required together: %s" % check)

    def _check_required_arguments(self):
        ''' ensure all required arguments are present '''
        missing = []
        for (k,v) in self.argument_spec.iteritems():
            required = v.get('required', False)
            if required and k not in self.params:
                missing.append(k)
        if len(missing) > 0:
            self.fail_json(msg="missing required arguments: %s" % ",".join(missing))

    def _check_argument_values(self):
        ''' ensure all arguments have the requested values, and there are no stray arguments '''
        for (k,v) in self.argument_spec.iteritems():
            choices = v.get('choices',None)
            if choices is None:
                continue
            if type(choices) == list:
                if k in self.params:
                    if self.params[k] not in choices:
                        choices_str=",".join([str(c) for c in choices])
                        msg="value of %s must be one of: %s, got: %s" % (k, choices_str, self.params[k])
                        self.fail_json(msg=msg)
            else:
                self.fail_json(msg="internal error: do not know how to interpret argument_spec")

    def _check_argument_types(self):
        ''' ensure all arguments have the requested type '''
        for (k, v) in self.argument_spec.iteritems():
            wanted = v.get('type', None)
            if wanted is None:
                continue
            if k not in self.params:
                continue

            value = self.params[k]
            is_invalid = False

            if wanted == 'str':
                if not isinstance(value, basestring):
                    self.params[k] = str(value)
            elif wanted == 'list':
                if not isinstance(value, list):
                    if isinstance(value, basestring):
                        self.params[k] = value.split(",")
                    elif isinstance(value, int) or isinstance(value, float):
                        self.params[k] = [ str(value) ]
                    else:
                        is_invalid = True
            elif wanted == 'dict':
                if not isinstance(value, dict):
                    if isinstance(value, basestring):
                        if value.startswith("{"):
                            try:
                                self.params[k] = json.loads(value)
                            except:
                                (result, exc) = self.safe_eval(value, dict(), include_exceptions=True)
                                if exc is not None:
                                    self.fail_json(msg="unable to evaluate dictionary for %s" % k)
                                self.params[k] = result
                        elif '=' in value:
                            self.params[k] = dict([x.split("=", 1) for x in value.split(",")])
                        else:
                            self.fail_json(msg="dictionary requested, could not parse JSON or key=value")
                    else:
                        is_invalid = True
            elif wanted == 'bool':
                if not isinstance(value, bool):
                    if isinstance(value, basestring):
                        self.params[k] = self.boolean(value)
                    else:
                        is_invalid = True
            elif wanted == 'int':
                if not isinstance(value, int):
                    if isinstance(value, basestring):
                        self.params[k] = int(value)
                    else:
                        is_invalid = True
            elif wanted == 'float':
                if not isinstance(value, float):
                    if isinstance(value, basestring):
                        self.params[k] = float(value)
                    else:
                        is_invalid = True
            else:
                self.fail_json(msg="implementation error: unknown type %s requested for %s" % (wanted, k))

            if is_invalid:
                self.fail_json(msg="argument %s is of invalid type: %s, required: %s" % (k, type(value), wanted))

    def _set_defaults(self, pre=True):
        for (k,v) in self.argument_spec.iteritems():
            default = v.get('default', None)
            if pre == True:
                # this prevents setting defaults on required items
                if default is not None and k not in self.params:
                    self.params[k] = default
            else:
                # make sure things without a default still get set None
                if k not in self.params:
                    self.params[k] = default

    def _load_params(self):
        ''' read the input and return a dictionary and the arguments string '''
        args = MODULE_ARGS
        items   = shlex.split(args)
        params = {}
        for x in items:
            try:
                (k, v) = x.split("=",1)
            except Exception, e:
                self.fail_json(msg="this module requires key=value arguments (%s)" % (items))
            params[k] = v
        params2 = json.loads(MODULE_COMPLEX_ARGS)
        params2.update(params)
        return (params2, args)

    def _log_invocation(self):
        ''' log that ansible ran the module '''
        # TODO: generalize a separate log function and make log_invocation use it
        # Sanitize possible password argument when logging.
        log_args = dict()
        passwd_keys = ['password', 'login_password']

        filter_re = [
            # filter out things like user:pass@foo/whatever
            # and http://username:pass@wherever/foo
            re.compile('^(?P<before>.*:)(?P<password>.*)(?P<after>\@.*)$'), 
        ]

        for param in self.params:
            canon  = self.aliases.get(param, param)
            arg_opts = self.argument_spec.get(canon, {})
            no_log = arg_opts.get('no_log', False)
                
            if no_log:
                log_args[param] = 'NOT_LOGGING_PARAMETER'
            elif param in passwd_keys:
                log_args[param] = 'NOT_LOGGING_PASSWORD'
            else:
                found = False
                for filter in filter_re:
                    if isinstance(self.params[param], unicode):
                        m = filter.match(self.params[param])
                    else:
                        m = filter.match(str(self.params[param]))
                    if m:
                        d = m.groupdict()
                        log_args[param] = d['before'] + "********" + d['after']
                        found = True
                        break
                if not found:
                    log_args[param] = self.params[param]

        module = 'ansible-%s' % os.path.basename(__file__)
        msg = ''
        for arg in log_args:
            if isinstance(log_args[arg], basestring):
                msg = msg + arg + '=' + log_args[arg].decode('utf-8') + ' '
            else:
                msg = msg + arg + '=' + str(log_args[arg]) + ' '
        if msg:
            msg = 'Invoked with %s' % msg
        else:
            msg = 'Invoked'

        # 6655 - allow for accented characters
        try:
            msg = msg.encode('utf8')
        except UnicodeDecodeError, e:
            pass

        if (has_journal):
            journal_args = ["MESSAGE=%s %s" % (module, msg)]
            journal_args.append("MODULE=%s" % os.path.basename(__file__))
            for arg in log_args:
                journal_args.append(arg.upper() + "=" + str(log_args[arg]))
            try:
                journal.sendv(*journal_args)
            except IOError, e:
                # fall back to syslog since logging to journal failed
                syslog.openlog(str(module), 0, syslog.LOG_USER)
                syslog.syslog(syslog.LOG_NOTICE, msg) #1
        else:
            syslog.openlog(str(module), 0, syslog.LOG_USER)
            syslog.syslog(syslog.LOG_NOTICE, msg) #2

    def _set_cwd(self):
        try:
            cwd = os.getcwd()
            if not os.access(cwd, os.F_OK|os.R_OK):
                raise
            return cwd
        except:
            # we don't have access to the cwd, probably because of sudo. 
            # Try and move to a neutral location to prevent errors
            for cwd in [os.path.expandvars('$HOME'), tempfile.gettempdir()]:
                try:
                    if os.access(cwd, os.F_OK|os.R_OK):
                        os.chdir(cwd)
                        return cwd
                except:
                    pass
        # we won't error here, as it may *not* be a problem, 
        # and we don't want to break modules unnecessarily
        return None    

    def get_bin_path(self, arg, required=False, opt_dirs=[]):
        '''
        find system executable in PATH.
        Optional arguments:
           - required:  if executable is not found and required is true, fail_json
           - opt_dirs:  optional list of directories to search in addition to PATH
        if found return full path; otherwise return None
        '''
        sbin_paths = ['/sbin', '/usr/sbin', '/usr/local/sbin']
        paths = []
        for d in opt_dirs:
            if d is not None and os.path.exists(d):
                paths.append(d)
        paths += os.environ.get('PATH', '').split(os.pathsep)
        bin_path = None
        # mangle PATH to include /sbin dirs
        for p in sbin_paths:
            if p not in paths and os.path.exists(p):
                paths.append(p)
        for d in paths:
            path = os.path.join(d, arg)
            if os.path.exists(path) and self.is_executable(path):
                bin_path = path
                break
        if required and bin_path is None:
            self.fail_json(msg='Failed to find required executable %s' % arg)
        return bin_path

    def boolean(self, arg):
        ''' return a bool for the arg '''
        if arg is None or type(arg) == bool:
            return arg
        if type(arg) in types.StringTypes:
            arg = arg.lower()
        if arg in BOOLEANS_TRUE:
            return True
        elif arg in BOOLEANS_FALSE:
            return False
        else:
            self.fail_json(msg='Boolean %s not in either boolean list' % arg)

    def jsonify(self, data):
        for encoding in ("utf-8", "latin-1", "unicode_escape"):
            try:
                return json.dumps(data, encoding=encoding)
            # Old systems using simplejson module does not support encoding keyword.
            except TypeError, e:
                return json.dumps(data)
            except UnicodeDecodeError, e:
                continue
        self.fail_json(msg='Invalid unicode encoding encountered')

    def from_json(self, data):
        return json.loads(data)

    def exit_json(self, **kwargs):
        ''' return from the module, without error '''
        self.add_path_info(kwargs)
        if not 'changed' in kwargs:
            kwargs['changed'] = False
        print self.jsonify(kwargs)
        sys.exit(0)

    def fail_json(self, **kwargs):
        ''' return from the module, with an error message '''
        self.add_path_info(kwargs)
        assert 'msg' in kwargs, "implementation error -- msg to explain the error is required"
        kwargs['failed'] = True
        print self.jsonify(kwargs)
        sys.exit(1)

    def is_executable(self, path):
        '''is the given path executable?'''
        return (stat.S_IXUSR & os.stat(path)[stat.ST_MODE]
                or stat.S_IXGRP & os.stat(path)[stat.ST_MODE]
                or stat.S_IXOTH & os.stat(path)[stat.ST_MODE])

    def digest_from_file(self, filename, digest_method):
        ''' Return hex digest of local file for a given digest_method, or None if file is not present. '''
        if not os.path.exists(filename):
            return None
        if os.path.isdir(filename):
            self.fail_json(msg="attempted to take checksum of directory: %s" % filename)
        digest = digest_method
        blocksize = 64 * 1024
        infile = open(filename, 'rb')
        block = infile.read(blocksize)
        while block:
            digest.update(block)
            block = infile.read(blocksize)
        infile.close()
        return digest.hexdigest()

    def md5(self, filename):
        ''' Return MD5 hex digest of local file using digest_from_file(). '''
        return self.digest_from_file(filename, _md5())

    def sha256(self, filename):
        ''' Return SHA-256 hex digest of local file using digest_from_file(). '''
        if not HAVE_HASHLIB:
            self.fail_json(msg="SHA-256 checksums require hashlib, which is available in Python 2.5 and higher")
        return self.digest_from_file(filename, _sha256())

    def backup_local(self, fn):
        '''make a date-marked backup of the specified file, return True or False on success or failure'''
        # backups named basename-YYYY-MM-DD@HH:MM~
        ext = time.strftime("%Y-%m-%d@%H:%M~", time.localtime(time.time()))
        backupdest = '%s.%s' % (fn, ext)

        try:
            shutil.copy2(fn, backupdest)
        except shutil.Error, e:
            self.fail_json(msg='Could not make backup of %s to %s: %s' % (fn, backupdest, e))
        return backupdest

    def cleanup(self,tmpfile):
        if os.path.exists(tmpfile):
            try:
                os.unlink(tmpfile)
            except OSError, e:
                sys.stderr.write("could not cleanup %s: %s" % (tmpfile, e))

    def atomic_move(self, src, dest):
        '''atomically move src to dest, copying attributes from dest, returns true on success
        it uses os.rename to ensure this as it is an atomic operation, rest of the function is
        to work around limitations, corner cases and ensure selinux context is saved if possible'''
        context = None
        dest_stat = None
        if os.path.exists(dest):
            try:
                dest_stat = os.stat(dest)
                os.chmod(src, dest_stat.st_mode & 07777)
                os.chown(src, dest_stat.st_uid, dest_stat.st_gid)
            except OSError, e:
                if e.errno != errno.EPERM:
                    raise
            if self.selinux_enabled():
                context = self.selinux_context(dest)
        else:
            if self.selinux_enabled():
                context = self.selinux_default_context(dest)

        creating = not os.path.exists(dest)

        try:
            # Optimistically try a rename, solves some corner cases and can avoid useless work, throws exception if not atomic.
            os.rename(src, dest)
        except (IOError,OSError), e:
            # only try workarounds for errno 18 (cross device), 1 (not permited) and 13 (permission denied)
            if e.errno != errno.EPERM and e.errno != errno.EXDEV and e.errno != errno.EACCES:
                self.fail_json(msg='Could not replace file: %s to %s: %s' % (src, dest, e))

            dest_dir = os.path.dirname(dest)
            dest_file = os.path.basename(dest)
            tmp_dest = tempfile.NamedTemporaryFile(
                prefix=".ansible_tmp", dir=dest_dir, suffix=dest_file)

            try: # leaves tmp file behind when sudo and  not root
                if os.getenv("SUDO_USER") and os.getuid() != 0:
                    # cleanup will happen by 'rm' of tempdir
                    # copy2 will preserve some metadata
                    shutil.copy2(src, tmp_dest.name)
                else:
                    shutil.move(src, tmp_dest.name)
                if self.selinux_enabled():
                    self.set_context_if_different(
                        tmp_dest.name, context, False)
                if dest_stat:
                    os.chown(tmp_dest.name, dest_stat.st_uid, dest_stat.st_gid)
                os.rename(tmp_dest.name, dest)
            except (shutil.Error, OSError, IOError), e:
                self.cleanup(tmp_dest.name)
                self.fail_json(msg='Could not replace file: %s to %s: %s' % (src, dest, e))

        if creating:
            # make sure the file has the correct permissions
            # based on the current value of umask
            umask = os.umask(0)
            os.umask(umask)
            os.chmod(dest, 0666 ^ umask)
            if os.getenv("SUDO_USER"):
                os.chown(dest, os.getuid(), os.getgid())

        if self.selinux_enabled():
            # rename might not preserve context
            self.set_context_if_different(dest, context, False)

    def run_command(self, args, check_rc=False, close_fds=False, executable=None, data=None, binary_data=False, path_prefix=None, cwd=None, use_unsafe_shell=False):
        '''
        Execute a command, returns rc, stdout, and stderr.
        args is the command to run
        If args is a list, the command will be run with shell=False.
        If args is a string and use_unsafe_shell=False it will split args to a list and run with shell=False
        If args is a string and use_unsafe_shell=True it run with shell=True.
        Other arguments:
        - check_rc (boolean)  Whether to call fail_json in case of
                              non zero RC.  Default is False.
        - close_fds (boolean) See documentation for subprocess.Popen().
                              Default is False.
        - executable (string) See documentation for subprocess.Popen().
                              Default is None.
        '''

        shell = False
        if isinstance(args, list):
            if use_unsafe_shell:
                args = " ".join([pipes.quote(x) for x in args])
                shell = True
        elif isinstance(args, basestring) and use_unsafe_shell:
            shell = True
        elif isinstance(args, basestring):
            args = shlex.split(args.encode('utf-8'))
        else:
            msg = "Argument 'args' to run_command must be list or string"
            self.fail_json(rc=257, cmd=args, msg=msg)

        # expand things like $HOME and ~
        if not shell:
            args = [ os.path.expandvars(os.path.expanduser(x)) for x in args ]

        rc = 0
        msg = None
        st_in = None

        # Set a temporart env path if a prefix is passed
        env=os.environ
        if path_prefix:
            env['PATH']="%s:%s" % (path_prefix, env['PATH'])

        # create a printable version of the command for use
        # in reporting later, which strips out things like
        # passwords from the args list
        if isinstance(args, list):
            clean_args = " ".join(pipes.quote(arg) for arg in args)
        else:
            clean_args = args

        # all clean strings should return two match groups, 
        # where the first is the CLI argument and the second 
        # is the password/key/phrase that will be hidden
        clean_re_strings = [
            # this removes things like --password, --pass, --pass-wd, etc.
            # optionally followed by an '=' or a space. The password can 
            # be quoted or not too, though it does not care about quotes
            # that are not balanced
            # source: http://blog.stevenlevithan.com/archives/match-quoted-string
            r'([-]{0,2}pass[-]?(?:word|wd)?[=\s]?)((?:["\'])?(?:[^\s])*(?:\1)?)',
            # TODO: add more regex checks here
        ]
        for re_str in clean_re_strings:
            r = re.compile(re_str)
            clean_args = r.sub(r'\1********', clean_args)

        if data:
            st_in = subprocess.PIPE

        kwargs = dict(
            executable=executable,
            shell=shell,
            close_fds=close_fds,
            stdin= st_in,
            stdout=subprocess.PIPE,
            stderr=subprocess.PIPE 
        )

        if path_prefix:
            kwargs['env'] = env
        if cwd and os.path.isdir(cwd):
            kwargs['cwd'] = cwd

        # store the pwd
        prev_dir = os.getcwd()

        # make sure we're in the right working directory
        if cwd and os.path.isdir(cwd):
            try:
                os.chdir(cwd)
            except (OSError, IOError), e:
                self.fail_json(rc=e.errno, msg="Could not open %s , %s" % (cwd, str(e)))

        try:
            cmd = subprocess.Popen(args, **kwargs)

            if data:
                if not binary_data:
                    data += '\n'
            out, err = cmd.communicate(input=data)
            rc = cmd.returncode
        except (OSError, IOError), e:
            self.fail_json(rc=e.errno, msg=str(e), cmd=clean_args)
        except:
            self.fail_json(rc=257, msg=traceback.format_exc(), cmd=clean_args)

        if rc != 0 and check_rc:
            msg = err.rstrip()
            self.fail_json(cmd=clean_args, rc=rc, stdout=out, stderr=err, msg=msg)

        # reset the pwd
        os.chdir(prev_dir)

        return (rc, out, err)

    def append_to_file(self, filename, str):
        filename = os.path.expandvars(os.path.expanduser(filename))
        fh = open(filename, 'a')
        fh.write(str)
        fh.close()

    def pretty_bytes(self,size):
        ranges = (
                (1<<70L, 'ZB'),
                (1<<60L, 'EB'),
                (1<<50L, 'PB'),
                (1<<40L, 'TB'),
                (1<<30L, 'GB'),
                (1<<20L, 'MB'),
                (1<<10L, 'KB'),
                (1, 'Bytes')
            )
        for limit, suffix in ranges:
            if size >= limit:
                break
        return '%.2f %s' % (float(size)/ limit, suffix)

def get_module_path():
    return os.path.dirname(os.path.realpath(__file__))

# only the command module should ever need to do this
# everything else should be simple key=value

class CommandModule(AnsibleModule):

    def _handle_aliases(self):
        return {}

    def _check_invalid_arguments(self):
        pass

    def _load_params(self):
        ''' read the input and return a dictionary and the arguments string '''
        args = MODULE_ARGS
        params = {}
        params['chdir'] = None
        params['creates'] = None
        params['removes'] = None
        params['shell'] = False
        params['executable'] = None
        if "#USE_SHELL" in args:
            args = args.replace("#USE_SHELL", "")
            params['shell'] = True

        r = re.compile(r'(^|\s)(creates|removes|chdir|executable|NO_LOG)=(?P<quote>[\'"])?(.*?)(?(quote)(?<!\\)(?P=quote))((?<!\\)(?=\s)|$)')
        for m in r.finditer(args):
            v = m.group(4).replace("\\", "")
            if m.group(2) == "creates":
                params['creates'] = v
            elif m.group(2) == "removes":
                params['removes'] = v
            elif m.group(2) == "chdir":
                v = os.path.expanduser(v)
                v = os.path.abspath(v)
                if not (os.path.exists(v) and os.path.isdir(v)):
                    self.fail_json(rc=258, msg="cannot change to directory '%s': path does not exist" % v)
                params['chdir'] = v
            elif m.group(2) == "executable":
                v = os.path.expanduser(v)
                v = os.path.abspath(v)
                if not (os.path.exists(v)):
                    self.fail_json(rc=258, msg="cannot use executable '%s': file does not exist" % v)
                params['executable'] = v
            elif m.group(2) == "NO_LOG":
                params['NO_LOG'] = self.boolean(v)
        args = r.sub("", args)
        params['args'] = args
        return (params, params['args'])

main()
