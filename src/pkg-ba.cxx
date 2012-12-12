#include "pkg-aa/h1d.hh"
#include "pkg-ab/h1d.hh"

#include <iostream>

int main(int, char**) 
{
  std::cout << "::: pkg-ba..." << std::endl
            << "::: testing pkg_aa..." << std::endl;
  pkg_aa::test_h1d();
  std::cout << "::: testing pkg_ab..." << std::endl;
  pkg_ab::test_h1d();
  std::cout << "::: done." << std::endl;
  return 0;
}
