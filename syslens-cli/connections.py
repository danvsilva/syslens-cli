import paramiko


def key_based_connect(bastion, username, ssh_key):
    pkey = paramiko.RSAKey.from_private_key_file(ssh_key)
    client = paramiko.SSHClient()
    policy = paramiko.AutoAddPolicy()
    client.set_missing_host_key_policy(policy)
    client.connect(bastion, username=username, pkey=pkey)
    return client


def jump_to_target(client, target, bastion_priv_ip):
    bastion_transport = client.get_transport()
    src_addr = (bastion_priv_ip, 22)
    dest_addr = (target, 22)
    bastion_channel = bastion_transport.open_channel(
        "direct-tcpip", dest_addr, src_addr
    )
    return bastion_channel
