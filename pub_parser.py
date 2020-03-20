import xml.etree.ElementTree as ET
import re

tree = ET.parse('SongShuaiwen.xml')

template = r"""<li><a href="{0}">"{1}"</a>&nbsp;{2}.&nbsp;In<a href="{3}"> {4}</a>.</li>""" + '\n'

leon = re.compile("^Shuaiwen (Leon )?Song$")
root = tree.getroot()\

conf_and_journal_info = {
    "ASAP2019" : ("IEEE International Conference on Application-specific Systems, Architectures and Processors (ASAP '19)", "https://ieeexplore.ieee.org/xpl/conhome/8812310/proceeding"),
    "ASPLOS2017" : ("Proceedings of the Twenty-Second International Conference on Architectural Support for Programming Languages and Operating Systems (ASPLOS '17)", "https://dl.acm.org/doi/proceedings/10.1145/3037697"),
    "CGO2018" : ("Proceedings of the 2018 International Symposium on Code Generation and Optimization (CGO '18)", "https://dl.acm.org/doi/proceedings/10.1145/3179541"),
    "CLUSTER2011" : ("IEEE International Conference on Cluster Computing (CLUSTER '11)", "https://ieeexplore.ieee.org/xpl/conhome/6059523/proceeding"),
    "CLUSTER2013" : ("IEEE International Conference on Cluster Computing (CLUSTER '13)", "https://ieeexplore.ieee.org/xpl/conhome/6689497/proceeding"),
    "DATE2016" : ("2016 Design, Automation & Test in Europe Conference & Exhibition (DATE)", "https://ieeexplore.ieee.org/xpl/conhome/7454909/proceeding"),
    "DATE2019" : ("2019 Design, Automation & Test in Europe Conference & Exhibition (DATE)", "https://ieeexplore.ieee.org/xpl/conhome/8704855/proceeding"),
    "E2SC@SC2013" : ("Proceedings of the 1st International Workshop on Energy Efficient Supercomputing (E2SC '13)", "https://dl.acm.org/doi/proceedings/10.1145/2536430"),
    "GreenCom/CPSCom2010" : ("2010 IEEE/ACM Int'l Conference on Green Computing and Communications & Int'l Conference on Cyber, Physical and Social Computing", "https://ieeexplore.ieee.org/xpl/conhome/5724111/proceeding"),
    "HPCA2017" : ("2017 IEEE International Symposium on High Performance Computer Architecture (HPCA)", "https://ieeexplore.ieee.org/xpl/conhome/7920262/proceeding"),
    "HPCA2018" : ("2018 IEEE International Symposium on High Performance Computer Architecture (HPCA)", "https://ieeexplore.ieee.org/xpl/conhome/8326505/proceeding"),
    "HPCA2019" : ("2019 IEEE International Symposium on High Performance Computer Architecture (HPCA)", "https://ieeexplore.ieee.org/xpl/conhome/8666628/proceeding"),
    "HPCC/CSS/ICESS2015" : ("2015 IEEE 17th International Conference on High Performance Computing and Communications, 2015 IEEE 7th International Symposium on Cyberspace Safety and Security, and 2015 IEEE 12th International Conference on Embedded Software and Systems", "https://ieeexplore.ieee.org/xpl/conhome/7335977/proceeding"),
    "HPDC2016" : ("Proceedings of the 25th ACM International Symposium on High-Performance Parallel and Distributed Computing (HPDC '16)", "https://dl.acm.org/doi/proceedings/10.1145/2907294"),
    "HiPC2010" : ("2010 International Conference on High Performance Computing (HiPC '10)", "https://ieeexplore.ieee.org/xpl/conhome/5708271/proceeding"),
    "ICPADS2014" : ("2014 20th IEEE International Conference on Parallel and Distributed Systems (ICPADS '14)", "https://ieeexplore.ieee.org/xpl/conhome/7092978/proceeding"),
    "ICS2014" : ("Proceedings of the 28th ACM international conference on Supercomputing (ICS '14)", "https://dl.acm.org/doi/proceedings/10.1145/2597652"),
    "ICS2015" : ("Proceedings of the 29th ACM on International Conference on Supercomputing (ICS '15)", "https://dl.acm.org/doi/proceedings/10.1145/2751205"),
    "ICS2016" : ("Proceedings of the 2016 International Conference on Supercomputing (ICS '16)", "https://dl.acm.org/doi/proceedings/10.1145/2925426"),
    "ICS2017" : ("Proceedings of the International Conference on Supercomputing (ICS '17)", "https://dl.acm.org/doi/proceedings/10.1145/3079079"),
    "ICS2018" : ("Proceedings of the 2018 International Conference on Supercomputing (ICS '18)", "https://dl.acm.org/doi/proceedings/10.1145/3205289"),
    "IEEE Trans. Parallel Distrib. Syst.2010" : ("IEEE Transactions on Parallel and Distributed Systems 2010", "https://ieeexplore.ieee.org/xpl/tocresult.jsp?isnumber=5439161"),
    "IEEE Trans. Parallel Distrib. Syst.2020" : ("IEEE Transactions on Parallel and Distributed Systems 2020", "https://ieeexplore.ieee.org/xpl/tocresult.jsp?isnumber=8935555"),
    "IISWC2018" : ("2018 IEEE International Symposium on Workload Characterization (IISWC '18)", "https://ieeexplore.ieee.org/xpl/conhome/8554060/proceeding"),
    "Int. J. High Perform. Comput. Appl.2009" : ("International Journal of High Performance Computing Applications 2009", "https://dl.acm.org/journal/sage-hpca"),
    "Int. J. High Perform. Comput. Appl.2014" : ("International Journal of High Performance Computing Applications 2014", "https://dl.acm.org/journal/sage-hpca"),
    "IPDPS Workshops2014" : ("2014 IEEE International Parallel and Distributed Processing Symposium Workshops (IPDPSW)", "https://ieeexplore.ieee.org/xpl/conhome/6967893/proceeding"),
    "IPDPS Workshops2015" : ("2015 IEEE International Parallel and Distributed Processing Symposium Workshops (IPDPSW)", "https://ieeexplore.ieee.org/xpl/conhome/7275194/proceeding"),
    "IPDPS Workshops2016" : ("2016 IEEE International Parallel and Distributed Processing Symposium Workshops (IPDPSW)", "https://ieeexplore.ieee.org/xpl/conhome/7518534/proceeding"),
    "IPDPS Workshops2017" : ("2017 IEEE International Parallel and Distributed Processing Symposium Workshops (IPDPSW)", "https://ieeexplore.ieee.org/xpl/conhome/7964630/proceeding"),
    "IPDPS Workshops2018" : ("2018 IEEE International Parallel and Distributed Processing Symposium Workshops (IPDPSW)", "https://ieeexplore.ieee.org/xpl/conhome/8424927/proceeding"),
    "IPDPS2011" : ("2011 IEEE International Parallel & Distributed Processing Symposium  (IPDPS '11)", "https://ieeexplore.ieee.org/xpl/conhome/6011824/proceeding"),
    "IPDPS2013" : ("2013 IEEE 27th International Symposium on Parallel and Distributed Processing (IPDPS '13)", "https://ieeexplore.ieee.org/xpl/conhome/6569024/proceeding"),
    "IPDPS2014" : ("2014 IEEE 28th International Parallel and Distributed Processing Symposium (IPDPS '14)", "https://ieeexplore.ieee.org/xpl/conhome/6875427/proceeding"),
    "IPDPS2015" : ("2015 IEEE International Parallel and Distributed Processing Symposium (IPDPS '15)", "https://ieeexplore.ieee.org/xpl/conhome/7159926/proceeding"),
    "IPDPS2016" : ("2016 IEEE International Parallel and Distributed Processing Symposium (IPDPS '16)", "https://ieeexplore.ieee.org/xpl/conhome/7510487/proceeding"),
    "ISC2017" : ("32nd International Conference, ISC High Performance 2017 (ISC '17)", "https://link.springer.com/book/10.1007/978-3-319-58667-0"),
    "ISCA2019" : ("Proceedings of the 46th International Symposium on Computer Architecture (ISCA '19)", "https://dl.acm.org/doi/proceedings/10.1145/3307650"),
    "J. Parallel Distributed Comput.2015" : ("Journal of Parallel and Distributed Computing 2015", "https://www.sciencedirect.com/journal/journal-of-parallel-and-distributed-computing"),
    "MASCOTS2012" : ("2012 IEEE 20th International Symposium on Modeling, Analysis and Simulation of Computer and Telecommunication Systems", "https://ieeexplore.ieee.org/xpl/conhome/6297612/proceeding"),
    "MCHPC@SC2017" : ("Proceedings of the Workshop on Memory Centric Programming for HPC (MCHPC '17)", "https://dl.acm.org/doi/proceedings/10.1145/3145617"),
    "MICRO2017" : ("Proceedings of the 50th Annual IEEE/ACM International Symposium on Microarchitecture (MICRO '17)", "https://dl.acm.org/doi/proceedings/10.1145/3123939"),
    "Middleware2016" : ("Proceedings of the 17th International Middleware Conference (Middleware '16)", "https://dl.acm.org/doi/proceedings/10.1145/2988336"),
    "PACT2012" : ("Proceedings of the 21st international conference on Parallel architectures and compilation techniques (PACT '12)", "https://dl.acm.org/doi/proceedings/10.1145/2370816"),
    "PACT2016" : ("Proceedings of the 2016 International Conference on Parallel Architectures and Compilation Techniques (PACT '16)", "https://dl.acm.org/doi/proceedings/10.1145/2967938"),
    "PPOPP2018" : ("Proceedings of the 23rd ACM SIGPLAN Symposium on Principles and Practice of Parallel Programming (PPoPP '18)", "https://dl.acm.org/doi/proceedings/10.1145/3178487"),
    "Parallel Processing Letters2014" : ("Parallel Processing Letters 2014", "https://www.worldscientific.com/worldscinet/ppl"),
    "SC Companion2012" : ("2012 SC Companion: High Performance Computing, Networking Storage and Analysis", "https://ieeexplore.ieee.org/xpl/conhome/6494369/proceeding"),
    "SC2015" : ("Proceedings of the International Conference for High Performance Computing, Networking, Storage and Analysis (SC '15)", "https://dl.acm.org/doi/proceedings/10.1145/2807591"),
    "SC2017" : ("Proceedings of the International Conference for High Performance Computing, Networking, Storage and Analysis (SC '17)", "https://dl.acm.org/doi/proceedings/10.1145/3126908"),
    "SC2019" : ("Proceedings of the International Conference for High Performance Computing, Networking, Storage and Analysis (SC '19)", "https://dl.acm.org/doi/proceedings/10.1145/3295500"),
    "TACO2016" : ("Transactions on Architecture and Code Optimization", "https://dl.acm.org/journal/taco"),
    "TACO2018" : ("Transactions on Architecture and Code Optimization", "https://dl.acm.org/journal/taco"),
    "The Journal of Supercomputing2013" : ("The Journal of Supercomputing", "https://link.springer.com/journal/11227")
}

def get_author_list(author_list):
    authors = map(lambda name: '<b>'+name.text+'</b>' if leon.match(name.text) else name.text, author_list)
    return ", ".join(authors)

def parse_journals(node):
    return template.format(node.find('ee').text,
    node.find('title').text.strip(), 
    get_author_list(node.findall('author')),
    conf_and_journal_info[node.find('journal').text+node.find('year').text][1],
    conf_and_journal_info[node.find('journal').text+node.find('year').text][0])

def parse_confs(node):
    return template.format(node.find('ee').text,
    node.find('title').text.strip(), 
    get_author_list(node.findall('author')),
    conf_and_journal_info[node.find('booktitle').text+node.find('year').text][1],
    conf_and_journal_info[node.find('booktitle').text+node.find('year').text][0])

result = []

for child in root:
    if child.tag == 'r':
        publication = child.getchildren()[0]

        if 'publtype' in publication.attrib and publication.attrib['publtype'] == 'informal':
            continue

        if publication.tag == 'article':
            result.append(parse_journals(publication))
        elif publication.tag == 'inproceedings':
            result.append(parse_confs(publication))
        else:
            raise Exception('Unexpected publication tag: ' + publication.tag)

with open ("temp_publication.html", "w") as out:
    out.writelines(result)